import tkinter as tk
from tkinter import Toplevel

def open_new_window():
    # Create a new window
    new_window = Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("300x200")

    # Add a label to the new window
    label = tk.Label(new_window, text="This is a new window")
    label.pack(pady=20)

    # Add a button to close the new window
    close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=10)

def main():
    global root
    # Create the main application window
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("400x300")

    # Add a button to open a new window
    open_button = tk.Button(root, text="Open New Window", command=open_new_window)
    open_button.pack(pady=50)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()