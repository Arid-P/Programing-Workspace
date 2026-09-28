# Import the tkinter module
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Tkinter LabelFrame Example")

# Create a LabelFrame widget
# A LabelFrame is a container widget with a border and an optional title.
label_frame = tk.LabelFrame(root, text="This is a LabelFrame", padx=10, pady=10)
label_frame.pack(padx=10, pady=10)

# Add a Label inside the LabelFrame
label = tk.Label(label_frame, text="This label is inside the LabelFrame.")
label.grid(row = 1, column = 1)
#while in a frame we can change if we use grid or pack 

# Start the Tkinter event loop
root.mainloop()