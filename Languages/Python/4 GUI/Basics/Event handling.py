import tkinter as tk

def main():
    """Main function to demonstrate event handling and commands in Tkinter."""
    
    # 1. Using the command parameter in buttons
    def on_button_click():
        """Function that gets called when the button is clicked."""
        print("Button clicked!")

    root1 = tk.Tk()
    root1.geometry("400x300")
    button1 = tk.Button(root1, text="Click Me", command=on_button_click)
    button1.pack()
    print("Running button example...")
    root1.mainloop()

    # 2. Binding events using the bind() method
    def on_left_click(event):
        """Handler for left mouse click."""
        print(f"Left clicked at ({event.x}, {event.y})")

    def on_key_press(event):
        """Handler for key press event."""
        print(f"Key pressed: {event.char}")

    root2 = tk.Tk()
    root2.geometry("500x400")
    root2.bind("<Button-1>", on_left_click)  # Left mouse click
    root2.bind("<KeyPress>", on_key_press)   # Key press
    print("Running event binding example...")
    root2.mainloop()

    # 4. Example of multiple event binding
    def on_mouse_motion(event):
        """Handler for mouse movement."""
        print(f"Mouse moved to ({event.x}, {event.y})")

    def on_enter(event):
        """Handler for mouse enter event."""
        print("Mouse entered the widget!")

    root3 = tk.Tk()
    root3.geometry("500x600")
    button3 = tk.Button(root3, text="Hover or Move Mouse", width=20)
    button3.pack()
    button3.bind("<Enter>", on_enter)
    button3.bind("<Motion>", on_mouse_motion)
    print("Running multiple event binding example...")
    root3.mainloop()

    # 5. Passing arguments with command and bind
    def on_button_click_with_argument(arg):
        """Button click handler with an argument."""
        print(f"Button clicked with argument: {arg}")

    root4 = tk.Tk()
    root4.geometry("400x300")
    button4 = tk.Button(root4, text="Click Me", command=lambda: on_button_click_with_argument("Hello"))
    button4.pack()
    print("Running command with arguments example...")
    root4.mainloop()

    def on_left_click_with_argument(event, arg):
        """Left click handler with an argument."""
        print(f"Left clicked at ({event.x}, {event.y}) with argument: {arg}")

    root5 = tk.Tk()
    root5.geometry("500x450")
    root5.bind("<Button-1>", lambda event: on_left_click_with_argument(event, "Click Info"))
    print("Running bind with arguments example...")
    root5.mainloop()

if __name__ == "__main__":
    main()