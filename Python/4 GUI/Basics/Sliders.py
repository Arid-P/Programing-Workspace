import tkinter as tk
from tkinter import ttk

def show_value():
    """
    Displays the current value of the slider in the label.
    """
    label.config(text=f"Slider Value: {slider.get()}")

def main():
    # Create the main application window
    root = tk.Tk()
    root.title("Tkinter Slider Example")
    root.geometry("400x300")

    # Create a vertical slider (Scale widget)
    global slider
    slider = ttk.Scale(
        root,  # Parent widget
        from_=0,  # Minimum value of the slider
        to=100,  # Maximum value of the slider
        orient="horizontal",  # Orientation of the slider
        command=lambda e: show_value()  # Update value dynamically
    )
    slider.set(50)  # Set the default position of the slider to 50
    slider.pack(pady=20)

    # Create a button to fetch and display the slider's value
    btn = ttk.Button(root, text="Get Slider Value", command=show_value)
    btn.pack(pady=10)

    # Create a label to display the current slider value
    global label
    label = tk.Label(root, text="Slider Value: 50", font=("Helvetica", 12))
    label.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()