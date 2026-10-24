from tkinter import Tk, Label, Button, DISABLED

root = Tk()
r = 5
def clicked_button() -> None:
    global r
    # Create a label that displays a message when the button is clicked
    Label(root, text="I clicked a button").grid(row=r, column=2)
    r = r+1
    return

def main() -> None:
    # Creating a button
    Button1 = Button(root, text="Click Me!")
    # Button is disabled
    Button2 = Button(root, text="Disabled Button", state=DISABLED)
    # Editing its size
    Button3 = Button(root, text="Large Button", padx=50, pady=50)
    # Adding color to it, fg for foreground color or text color and bg for background color
    Button4 = Button(root, text="Colored Button", fg="red", bg="#fc8484")
    # Creating a functional button
    Button5 = Button(root, text="Functional Button", command=clicked_button)
    
    # Putting the buttons on screen
    Button1.grid(row=0, column=4)
    Button2.grid(row=1, column=4)
    Button3.grid(row=2, column=2)
    Button4.grid(row=3, column=4)
    Button5.grid(row=4, column=4)
    
    # Start the Tkinter event loop
    root.mainloop()
    return

if __name__ == "__main__":
    main()