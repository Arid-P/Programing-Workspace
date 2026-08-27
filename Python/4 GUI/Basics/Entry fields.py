import tkinter as tk

root = tk.Tk()

def submit_input():
    """
    Function to handle the submission of input.
    It retrieves the input from the Entry widget and displays it in the Label.
    """
    user_input = in_val.get()  # Get the text from the in_val widget
    tk.Label(root, text=f"You entered: {user_input}").pack(pady=5) # Display the input in the label

def main():
    """
    Main function to create the Tkinter GUI application.
    """
    global in_val  # Declare the entry variable global variables to access them inside other functions

    # Create a label to prompt the user
    prompt_label = tk.Label(root, text="Enter something:")
    prompt_label.pack(pady=5)

    # Create an Entry widget to take user input
    in_val = tk.Entry(root, width=30)
    in_val.pack(pady=5)

    # Create a button to submit the input
    submit_button = tk.Button(root, text="Submit", command=submit_input)
    submit_button.pack(pady=5)

    # Create a label to display the output

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()