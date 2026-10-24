import tkinter as tk
from tkinter import ttk

def show_selection():
    """
    Displays the current states of the checkboxes.
    """
    # Fetch the states of each checkbox
    selections = f"Python: {python_var.get()}, Java: {java_var.get()}, C++: {cpp_var.get()}"
    label.config(text=f"Selections: {selections}")

def main():
    # Create the main application window
    root = tk.Tk()
    root.title("Tkinter Checkboxes Example")
    root.geometry("400x300")

    # Create variables to track the state of each checkbox
    global python_var, java_var, cpp_var
    python_var = tk.IntVar()  # Tracks Python checkbox (1 for checked, 0 for unchecked)
    java_var = tk.IntVar()    # Tracks Java checkbox
    cpp_var = tk.IntVar()     # Tracks C++ checkbox

    # Create Checkbuttons
    python_cb = ttk.Checkbutton(root, text="Python", variable=python_var, command=show_selection)
    java_cb = ttk.Checkbutton(root, text="Java", variable=java_var, command=show_selection)
    cpp_cb = ttk.Checkbutton(root, text="C++", variable=cpp_var, command=show_selection)

    # Pack the checkboxes
    python_cb.pack(pady=5, anchor="w")  # Align to the left (west)
    java_cb.pack(pady=5, anchor="w")
    cpp_cb.pack(pady=5, anchor="w")

    # Create a label to display the current checkbox selections
    global label
    label = tk.Label(root, text="Selections: None", font=("Helvetica", 12))
    label.pack(pady=10)

    # Create a button to explicitly show the current selection
    btn = ttk.Button(root, text="Show Selection", command=show_selection)
    btn.pack(pady=20)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()