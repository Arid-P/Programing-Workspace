import tkinter as tk
from tkinter import messagebox, filedialog

# Functionality for menu commands
def open_file() -> None:
    """Open a file using a file dialog."""
    file_path = filedialog.askopenfilename(
        title="Open File", 
        filetypes=(("Python Files", "*.py"), ("Text Files", "*.txt"), ("C plus plus Files", "*.cpp"), ("All Files", "*.*"))
    )
    if file_path:
        print(f"File selected: {file_path}")

def save_file() -> None:
    """Save a file using a file dialog."""
    file_path = filedialog.asksaveasfilename(
        title="Save File", 
        defaultextension=".txt",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if file_path:
        print(f"File saved at: {file_path}")

def show_message() -> None:
    """Show an informational message."""
    messagebox.showinfo("Information", "This is an informational alert!")

def create_gui() -> None:
    """Create the main GUI window."""
    # Main Window
    root = tk.Tk()
    root.title("Menus and Dialogs Example")
    root.geometry("400x200")

    # Menus: Creating a Menu Bar
    menu_bar = tk.Menu(root)

    # File Menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Open", command=open_file)  # Add "Open" command
    file_menu.add_command(label="Save", command=save_file)  # Add "Save" command
    file_menu.add_separator()  # Add a separator line
    file_menu.add_command(label="Exit", command=root.quit)  # Add "Exit" command
    menu_bar.add_cascade(label="File", menu=file_menu)  # Add File menu to the menu bar

    # Help Menu
    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="About", command=show_message)  # Add "About" command
    menu_bar.add_cascade(label="Help", menu=help_menu)  # Add Help menu to the menu bar

    # Configuring the Menu Bar
    root.config(menu=menu_bar)

    # Main Loop
    root.mainloop()

def main() -> None:
    """Main function to start the application."""
    create_gui()

if __name__ == "__main__":
    main()