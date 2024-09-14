Tentu! Berikut adalah contoh README yang bisa Anda gunakan untuk program pengecekan folder:

---

# Storage Checking

## Overview

This program helps you analyze and check the size of folders within a specified directory. It calculates the size of each folder and lists them in descending order based on their size. The program skips empty folders and provides real-time updates on the size of folders being processed.

## Features

- Calculates and displays the size of each folder.
- Skips empty folders and provides a message indicating their emptiness.
- Lists folders that are larger than 500MB.
- Allows you to navigate into subdirectories and repeat the process.

## Installation

To use this program, you need Python installed on your machine. No additional libraries are required.

## Usage

1. **Clone or download the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the program**:
   ```bash
   python storage_check.py
   ```

3. **Input the directory path** when prompted. The program will start analyzing the specified directory.

4. **Follow the prompts**:
   - After scanning the initial directory, you can choose to continue with a subdirectory.
   - The program will list subdirectories larger than 500MB and allow you to select one to analyze further.

## Example

Here's an example of how the program's output might look:

```text
Input directory: C:\Users

Scanning 'Documents': 1000 files [01:10, 950 files/s] Size so far: 200.0 MiB
Folder 'Documents' with size 200.1 MiB completed.
--------------------------------------------------
Scanning 'Downloads': 500 files [00:45, 1100 files/s] Size so far: 350.5 MiB
Folder 'Downloads' with size 350.6 MiB completed.
--------------------------------------------------

Folders in 'C:\Users' sorted by size (GB):

Documents: 200.1 MiB
Downloads: 350.6 MiB

==================================================
```

## Notes

- The program uses the `humanize` library to format sizes for readability.
- Ensure the directory path provided exists and you have sufficient permissions to access it.

## Contributing

Feel free to fork the repository and submit pull requests. Any improvements or bug fixes are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Adjust the paths and repository details as necessary. Let me know if you need any changes!
