

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
2. **install requirement**:
   ```terminal
   pip install humanize
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
IInput directory : D:\EMULATOR GAME
Folder EMULATOR GAME\DOLPHIN: 59.5 MiB
--------------------------------------------------
Folder EMULATOR GAME\PCSX2 1.6.0: 55.3 MiB
--------------------------------------------------
Folder EMULATOR GAME\SWITCH: 108.9 MiB
--------------------------------------------------
Folder EMULATOR GAME\yuzu: 418.3 MiB
--------------------------------------------------

Folders in D:\EMULATOR GAME sorted by size (GB):

SWITCH: 200.1 MiB
YUZU: 350.6 MiB

==================================================
```

## Notes

- The program uses the `humanize` library to format sizes for readability.
- Ensure the directory path provided exists and you have sufficient permissions to access it.
- the programs just display folder that have size more than 500MB, you can adjust whenever you like

## Contributing

Feel free to fork the repository and submit pull requests. Any improvements or bug fixes are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Adjust the paths and repository details as necessary. Let me know if you need any changes!
