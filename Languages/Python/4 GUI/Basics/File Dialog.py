import tkinter as tk
from tkinter import filedialog

def open_file():
    # Open a file dialog and store the selected file path
    file_path = filedialog.askopenfilename(
        initialdir="/storage/emulated/0/Programing/Python/Gui/Basics/Images",  # Starting directory for the dialog
        title="Select A File",  # Dialog title
        filetypes=(("Jpg files", "*.jpg"), ("Png files", "*.png"), ("Python files", "*.py"), ("All files", "*.*"))  # File types filter
    )
    # Display the selected file path in the label
    if file_path:
        label.config(text=f"Selected File: {file_path}")
    else:
        label.config(text="No file selected")

def main():
    # Create the main application window
    root = tk.Tk()
    root.title("File Dialog Example")
    root.geometry("400x200")

    # Create a button to open the file dialog
    open_button = tk.Button(root, text="Open File", command=open_file)
    open_button.pack(pady=20)

    # Create a label to display the selected file path
    global label
    label = tk.Label(root, text="No file selected")
    label.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()