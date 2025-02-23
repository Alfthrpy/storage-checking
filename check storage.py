import os
import humanize
from multiprocessing import Pool
from tqdm import tqdm
from tabulate import tabulate  # pastikan sudah diinstall dengan: pip install tabulate

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_size(start_path):
    """Menghitung ukuran total folder secara real-time"""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
    return total_size

def format_size(size_in_bytes):
    return humanize.naturalsize(size_in_bytes, binary=True)

def get_folders_sorted_by_size(directory):
    folder_list = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    folder_sizes = []
    with Pool(10) as pool:
        full_paths = [os.path.join(directory, folder) for folder in folder_list]
        for size in tqdm(pool.imap(get_size, full_paths),
                         total=len(folder_list), desc="Calculating sizes", ncols=70):
            folder_sizes.append(size)
    folders_with_sizes = list(zip(folder_list, folder_sizes))
    folders_with_sizes.sort(key=lambda x: x[1], reverse=True)
    return folders_with_sizes

def display_folders(folders_with_sizes, directory):
    header = f"Direktori saat ini: {directory}"
    print('\n'+header)
    
    if not folders_with_sizes:
        print("Tidak ada subfolder di direktori ini.")
    else:
        # Menyiapkan data untuk tabulate
        table_data = []
        for i, (folder, size) in enumerate(folders_with_sizes, start=1):
            table_data.append([i, folder, format_size(size)])
        print(tabulate(table_data, headers=["No", "Subfolder", "Ukuran"], tablefmt="fancy_grid"))
    print()

def main():
    root_directory = input("Input direktori (root): ").strip()
    if not os.path.isdir(root_directory):
        print("Direktori tidak valid!")
        return

    history = [root_directory]
    cache = {}

    while True:
        clear_console()
        current_directory = history[-1]

        if current_directory in cache:
            folders_with_sizes = cache[current_directory]
        else:
            folders_with_sizes = get_folders_sorted_by_size(current_directory)
            cache[current_directory] = folders_with_sizes

        display_folders(folders_with_sizes, current_directory)
        print("Menu:")
        print("1. Masuk ke subfolder")
        print("2. Kembali ke direktori sebelumnya")
        print("3. Keluar")
        pilihan = input("\nMasukkan pilihan Anda (1/2/3): ").strip().lower()

        if pilihan == '1':
            if not folders_with_sizes:
                input("\nTidak ada subfolder. Tekan Enter untuk kembali...")
                continue

            try:
                pil = int(input("\nPilih nomor subfolder: "))
                if 1 <= pil <= len(folders_with_sizes):
                    subfolder = folders_with_sizes[pil - 1][0]
                    new_directory = os.path.join(current_directory, subfolder)
                    history.append(new_directory)
                else:
                    input("\nPilihan tidak valid. Tekan Enter untuk melanjutkan...")
            except ValueError:
                input("\nInput tidak valid! Harap masukkan angka. Tekan Enter untuk melanjutkan...")
                
        elif pilihan == '2':
            if len(history) == 1:
                input("\nAnda sudah berada di direktori root. Tekan Enter untuk melanjutkan...")
            else:
                history.pop()
        elif pilihan == '3':
            print("Program selesai.")
            break
        else:
            input("\nPilihan tidak dikenali, tekan Enter untuk mencoba lagi.")

if __name__ == "__main__":
    main()
