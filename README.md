

# Storage Checking

## Overview

This program helps you analyze and check the size of folders within a specified directory. It calculates the size of each folder and lists them in descending order based on their size.

## Features

- Calculates and displays the size of each folder.
- Allows you to navigate into subdirectories and repeat the process.

## Installation

To use this program, you need Python installed on your machine. Alternatively, you can [download the executable file](https://github.com/Alfthrpy/storage-checking/releases/download/storage-cheking/check_storage.exe) from the Releases page.

## Usage with cloning project

1. **Clone or download the repository**:
   ```bash
   git clone https://github.com/Alfthrpy/storage-checking
   cd storage-checking
   ```
2. **install requirement**:
   ```terminal
   pip install -r requirements.txt
   ```

2. **Run the program**:
   ```bash
   python check_storage.py
   ```

3. **Input the directory path** when prompted. The program will start analyzing the specified directory.

4. **Follow the prompts**:
   - After scanning the initial directory, you can choose to continue with a subdirectory.
   - The program will list subdirectories larger than 500MB and allow you to select one to analyze further.

## Or you can download the executable program and run it on your computer

## Example

Here's an example of how the program's output might look:

```text
Input direktori (root): D:\Games

Calculating sizes: 100%|████████████████| 5/5 [00:01<00:00,  4.72it/s]

Direktori saat ini: D:\Games
╒══════╤═══════════════════════════════════════════════════════════╤═══════════╕
│   No │ Subfolder                                                 │ Ukuran    │
╞══════╪═══════════════════════════════════════════════════════════╪═══════════╡
│    1 │ Elden Ring                                                │ 68.0 GiB  │
├──────┼───────────────────────────────────────────────────────────┼───────────┤
│    2 │ WorldWarZ                                                 │ 66.7 GiB  │
├──────┼───────────────────────────────────────────────────────────┼───────────┤
│    3 │ Epic Games                                                │ 1.0 GiB   │
├──────┼───────────────────────────────────────────────────────────┼───────────┤
│    4 │ Balatro.v1.0.1m                                           │ 132.2 MiB │
├──────┼───────────────────────────────────────────────────────────┼───────────┤
│    5 │ EldenRing-Save-Manager-v1.73-portable-214-1-73-1709394075 │ 77.5 MiB  │
╘══════╧═══════════════════════════════════════════════════════════╧═══════════╛

Menu:
1. Masuk ke subfolder
2. Kembali ke direktori sebelumnya
3. Keluar

Masukkan pilihan Anda (1/2/3):
```

## Notes

- The program uses the `humanize`, `tabulate` and `tqdm` library to format sizes for readability.
- Ensure the directory path provided exists and you have sufficient permissions to access it.
- the programs just display folder that have size more than 500MB, you can adjust whenever you like

## Contributing

Feel free to fork the repository and submit pull requests. Any improvements or bug fixes are welcome!


