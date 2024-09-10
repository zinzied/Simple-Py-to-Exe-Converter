# Py to Exe Converter

This script provides a graphical user interface (GUI) for converting Python scripts (`.py` files) to executable files (`.exe`) using PyInstaller. The GUI is built using `tkinter` and includes options for selecting the Python file, output directory, output format (`onefile` or `onedir`), window option (console or windowed), and an optional icon file.

## Features

- **File Selection**: Browse and select the Python script to convert.
- **Output Directory**: Choose the directory where the executable will be saved.
- **Output Format**: Select between `onefile` (single executable) or `onedir` (directory with dependencies).
- **Window Option**: Choose whether to show the console window or hide it (windowed mode).
- **Icon File**: Optionally add an icon to the executable.
- **Progress Bar**: Displays a progress bar while the conversion is in progress to indicate activity.
- **Threading**: Uses threading to ensure the GUI remains responsive during the conversion process.

## Usage

1. **Install PyInstaller**: Ensure you have PyInstaller installed. You can install it using pip:
   ```sh
   pip install pyinstaller
   ```

2. **Run the Script**: Execute the script using Python:
   ```sh
   python py2exe.py
   ```

3. **Select Python File**: Click the "Browse" button next to the "Python file" field to select the `.py` file you want to convert.

4. **Select Output Directory**: Click the "Browse" button next to the "Output directory" field to choose where the executable will be saved.

5. **Choose Output Option**: Select either "Onefile" or "Onedir" for the output format.

6. **Choose Window Option**: Select either "Console" or "Windowed" to determine whether the console window should be shown.

7. **Optional Icon**: If you want to add an icon to the executable, click the "Browse" button next to the "Icon file (optional)" field and select an `.ico` file.

8. **Convert**: Click the "Convert" button to start the conversion process. The progress bar will indicate that the process is ongoing.

9. **Completion**: A message box will notify you whether the conversion was successful or if it failed.

## ScreenShot

![image](https://github.com/user-attachments/assets/13c2751d-b6ec-4256-a604-5f58a5065f64)



This script simplifies the process of converting Python scripts to executables, making it accessible even for users who are not familiar with command-line tools.
