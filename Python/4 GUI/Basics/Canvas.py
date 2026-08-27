import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk  # For displaying images

import os

def change_dir() -> None:
    os.chdir("/storage/emulated/0/Programing/Python/GUI/Basics/Images") 
    return

def main() -> None:
    """Main function to create and display canvas elements."""
    # Create main window
    root = tk.Tk()
    root.title("Canvas Example")
    root.geometry("600x400")

    # Create Canvas widget
    canvas = Canvas(root, width=600, height=400, bg="white")
    canvas.pack()

    # Drawing Shapes
    # 1. Line
    canvas.create_line(50, 50, 200, 50, fill="blue", width=3)  # x1, y1, x2, y2
    canvas.create_line(50, 70, 200, 120, fill="red", dash=(4, 2))  # Dashed line

    # 2. Rectangle
    canvas.create_rectangle(250, 50, 400, 150, outline="black", fill="green", width=2)

    # 3. Oval (Ellipse or Circle)
    canvas.create_oval(50, 200, 200, 350, outline="purple", fill="yellow", width=3)

    # 4. Polygon
    canvas.create_polygon(300, 200, 350, 300, 450, 250, 400, 150, outline="black", fill="orange", width=2)

    # 5. Text
    canvas.create_text(300, 50, text="Hello, Canvas!", font=("Arial", 16), fill="darkblue")

    # Displaying Images (requires PIL library)
    # Load and resize the image
    image = Image.open("Shruti 1.jpg").resize((100, 100)) 
    image_tk = ImageTk.PhotoImage(image)
    canvas.create_image(500, 300, image=image_tk)  # x, y coordinates

    # Keep the reference to the image to prevent garbage collection
    canvas.image = image_tk

    root.mainloop()

if __name__ == "__main__":
    change_dir()
    main()