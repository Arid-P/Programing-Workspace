# Notes on Dropdown Menus in Tkinter (tk module)

# Introduction to Dropdown Menus
# A dropdown menu (also called an OptionMenu in Tkinter) allows users to select an option from a list.
# This is useful for creating selection-based user interfaces.

# Importing Tkinter
import tkinter as tk

# Function to create the main application window
def main():
    # Creating the main window
    root = tk.Tk()
    root.title("Dropdown Menu Example")

    # Creating a StringVar to store the selected value
    selected_option = tk.StringVar()
    selected_option.set("Select an option")  # Default value

    # Creating an OptionMenu
    # The first parameter is the parent widget (root), the second is the StringVar to store the selection,
    # followed by the list of options.
    options = ["Option 1", "Option 2", "Option 3", "Option 4"]
    dropdown = tk.OptionMenu(root, selected_option, *options)
    dropdown.pack(pady=10)

    # Function to display the selected option
    def show_selection():
        print(f"Selected option: {selected_option.get()}")

    # Button to display the selected option
    button = tk.Button(root, text="Show Selection", command=show_selection)
    button.pack(pady=10)

    # Customizing the Dropdown Menu
    # The OptionMenu widget itself does not support direct styling, but its menu part can be customized.
    # The menu of an OptionMenu can be accessed using `.children`.
    menu = dropdown.children["menu"]
    menu.configure(font=("Arial", 12), background="lightblue", foreground="black")

    # Running the Tkinter main event loop
    root.mainloop()

# Ensuring the script runs only when executed directly
if __name__ == "__main__":
    main()

# Summary
# - `tk.OptionMenu` is used for creating dropdown menus in Tkinter.
# - A `StringVar` stores the selected value.
# - The `.children["menu"]` property allows customization of the dropdown's appearance.
# - Dropdown menus are useful for user selection in GUI applications.

# By understanding how to use and customize dropdown menus, you can enhance your Tkinter applications effectively!

