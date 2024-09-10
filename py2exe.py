import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    entry_file_path.delete(0, tk.END)
    entry_file_path.insert(0, file_path)

def browse_output_dir():
    output_dir = filedialog.askdirectory()
    entry_output_dir.delete(0, tk.END)
    entry_output_dir.insert(0, output_dir)

def convert():
    file_path = entry_file_path.get()
    output_dir = entry_output_dir.get()
    if not file_path:
        messagebox.showerror("Error", "Please select a Python file to convert.")
        return
    if not output_dir:
        messagebox.showerror("Error", "Please select an output directory.")
        return

    output_option = var_output_option.get()
    window_option = var_window_option.get()
    icon_path = entry_icon_path.get()

    command = ["pyinstaller", file_path, "--distpath", output_dir]

    if output_option == "onefile":
        command.append("--onefile")
    if window_option == "windowed":
        command.append("--noconsole")
    if icon_path:
        command.extend(["--icon", icon_path])

    progress_bar.start()
    try:
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", "Conversion completed successfully.")
    except subprocess.CalledProcessError as e:
        log_file_path = os.path.join(output_dir, "conversion_error.log")
        with open(log_file_path, "w") as log_file:
            log_file.write(str(e))
        messagebox.showerror("Error", f"Conversion failed: {e}. See log file at {log_file_path}")
    finally:
        progress_bar.stop()

def start_conversion():
    threading.Thread(target=convert).start()

app = tk.Tk()
app.title("Py to Exe Converter")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

label_file_path = tk.Label(frame, text="Python file:")
label_file_path.grid(row=0, column=0, sticky="e")

entry_file_path = tk.Entry(frame, width=50)
entry_file_path.grid(row=0, column=1, padx=5)

button_browse = tk.Button(frame, text="Browse", command=browse_file)
button_browse.grid(row=0, column=2)

label_output_option = tk.Label(frame, text="Output option:")
label_output_option.grid(row=1, column=0, sticky="e")

var_output_option = tk.StringVar(value="onefile")
radio_onefile = tk.Radiobutton(frame, text="Onefile", variable=var_output_option, value="onefile")
radio_onefile.grid(row=1, column=1, sticky="w")

radio_onedir = tk.Radiobutton(frame, text="Onedir", variable=var_output_option, value="onedir")
radio_onedir.grid(row=1, column=2, sticky="w")

label_window_option = tk.Label(frame, text="Window option:")
label_window_option.grid(row=2, column=0, sticky="e")

var_window_option = tk.StringVar(value="console")
radio_console = tk.Radiobutton(frame, text="Console", variable=var_window_option, value="console")
radio_console.grid(row=2, column=1, sticky="w")

radio_windowed = tk.Radiobutton(frame, text="Windowed", variable=var_window_option, value="windowed")
radio_windowed.grid(row=2, column=2, sticky="w")

label_icon_path = tk.Label(frame, text="Icon file (optional):")
label_icon_path.grid(row=3, column=0, sticky="e")

entry_icon_path = tk.Entry(frame, width=50)
entry_icon_path.grid(row=3, column=1, padx=5)

button_browse_icon = tk.Button(frame, text="Browse", command=lambda: entry_icon_path.insert(0, filedialog.askopenfilename(filetypes=[("Icon files", "*.ico")])))
button_browse_icon.grid(row=3, column=2)

label_output_dir = tk.Label(frame, text="Output directory:")
label_output_dir.grid(row=4, column=0, sticky="e")

entry_output_dir = tk.Entry(frame, width=50)
entry_output_dir.grid(row=4, column=1, padx=5)

button_browse_output = tk.Button(frame, text="Browse", command=browse_output_dir)
button_browse_output.grid(row=4, column=2)

button_convert = tk.Button(app, text="Convert", command=start_conversion)
button_convert.pack(pady=10)

progress_bar = ttk.Progressbar(app, mode='indeterminate')
progress_bar.pack(pady=10)

app.mainloop()