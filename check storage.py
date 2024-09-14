import os
import humanize
import sys

def get_size(start_path):
    """Fungsi untuk menghitung ukuran total folder secara real-time"""
    total_size = 0
    files_found = False
    for dirpath, dirnames, filenames in os.walk(start_path):
        if filenames:
            files_found = True
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
                # Tampilkan ukuran yang sudah terbaca secara sementara
                sys.stdout.write(f"\rFolder {start_path[3:]}: {humanize.naturalsize(total_size, binary=True)}")
                sys.stdout.flush()
    print()
    if not files_found:
        pass
    return total_size

def format_size(size_in_bytes):
    """Format ukuran dari bytes ke GB"""
    return humanize.naturalsize(size_in_bytes, binary=True)

def get_folders_sorted_by_size(directory):
    """Mengembalikan daftar folder diurutkan berdasarkan ukuran"""
    folder_sizes = []
    folder_list = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    
    for folder in folder_list:
        folder_path = os.path.join(directory, folder)
        folder_size = get_size(folder_path)
        
        # Tampilkan pesan jika folder lebih dari 500MB
        if folder_size > 524288000:
            folder_sizes.append((folder, folder_size))
        elif folder_size == 0:
            print(f"Folder {folder}:")
        print("-" * 50)  # Pisahkan setiap folder dengan garis
    return folder_sizes

def display_folders(folders_with_sizes, directory):
    """Menampilkan folder yang diurutkan berdasarkan ukuran"""
    print(f"\nFolder di '{directory}' diurutkan berdasarkan ukuran (GB):\n")
    for folder, size in folders_with_sizes:
        print(f"{folder}: {format_size(size)}")
    print("\n" + "=" * 50)

def main():
    directory = input("Input directory : ")

    while True:
        folders_with_sizes = get_folders_sorted_by_size(directory)
        display_folders(folders_with_sizes, directory)

        pil = input("\nApakah ingin lanjutkan penghitungan? (y/n): ").strip().lower()
        if pil == 'y':
            print("Direktori mana yang ingin dilanjutkan:")
            for i, (folder, _) in enumerate(folders_with_sizes):
                print(f"{i + 1} | {folder}")
            
            try:
                pil_dir = int(input("Pilihan Anda: "))
                if 1 <= pil_dir <= len(folders_with_sizes):
                    dir_pil = folders_with_sizes[pil_dir - 1][0]
                    directory = os.path.join(directory, dir_pil)
                else:
                    print("Pilihan tidak valid!")
            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")
        else:
            print("Proses selesai.")
            break

if __name__ == "__main__":
    main()
