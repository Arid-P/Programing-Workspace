# Import the tkinter module
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Tkinter Radiobutton Example")

# Function to display the selected option
def show_selection():
    selection_label.config(text=f"Selected: {selected_option.get()}")

def main () :
    global selected_option, selection_label
    # Define a Tkinter variable to hold the value of the selected radiobutton
    selected_option = tk.StringVar()
    selected_option.set("Option ")  # Set a default value

    # Create Radiobuttons
    # Radiobuttons allow the user to select one option from a set.
    radio1 = tk.Radiobutton(root, text="Option 1", variable=selected_option, value="Option 1", command=show_selection)
    radio2 = tk.Radiobutton(root, text="Option 2", variable=selected_option, value="Option 2", command=show_selection)
    radio3 = tk.Radiobutton(root, text="Option 3", variable=selected_option, value="Option 3", command=show_selection)
    
    # Pack the Radiobuttons
    radio1.pack(anchor='w')
    radio2.pack(anchor='w')
    radio3.pack(anchor='w')
    
    # Label to display the selected option
    selection_label = tk.Label(root, text="Selected: Option None")
    selection_label.pack()
    
    # Start the Tkinter event loop
    root.mainloop()


main()