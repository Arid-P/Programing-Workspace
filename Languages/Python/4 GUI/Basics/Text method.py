import tkinter as tk

root = tk.Tk()
root.title("Tkinter Text Widget Example")
    
def get_text_content(text_box: tk.Text) -> None:
    """
    Retrieves and prints the content of the Text widget when the button is clicked.
    
    :param text_box: The Text widget from which to fetch the content.
    """
    #here 1.0 means line.column i.e. from which line and column do we start to get the text from
    content = text_box.get("1.0", tk.END)  # Fetch text from the start to the end
    tk.Label(root, text="Text content:\n" + content).pack()


def main() -> None:
    """
    Main function to set up the Tkinter application.
    """

    # Create a Text widget
    text_box = tk.Text(
        root,
        height=10,
        width=40,
        wrap=tk.WORD,
        font=("Arial", 12),
        bg="lightyellow",
        fg="black"
    )
    text_box.pack(pady=10)

    # Add default text to the Text widget
    text_box.insert(tk.END, "Welcome to the Tkinter Text widget!\nYou can edit this text.")

    # Add a button to fetch and print the text content
    btn_get_text = tk.Button(
        root,
        text="Get Text",
        command=lambda: get_text_content(text_box)  # Pass text_box to the function
    )
    btn_get_text.pack(pady=5)

    # Start the Tkinter main event loop
    root.mainloop()

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()