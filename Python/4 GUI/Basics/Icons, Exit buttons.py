# Import the necessary modules from tkinter and PIL (Pillow)
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os

def change_dir() -> None:
    tk.Label(root, text=os.getcwd()).pack()
    os.chdir("/storage/emulated/0/Programing/Python/GUI/Basics/Images") 
    tk.Label(root, text=os.getcwd()).pack()
    return

# Create the main application window
root = tk.Tk()
root.title("Tkinter Icons, Images, and Exit Button")

# Define a function to close the application
def exit_app():
    root.destroy()

def main() -> None:
    # Set the window icon (Optional)
    # root.iconbitmap('0 download.ico')
    
    # IMAGE HANDLING SECTION
    
    # Step 1: Open the first image
    image = Image.open('Shruti and me 1.jpg')
    
    # Step 1.5: Resizing the Image
    target_width, target_height = 800, 600
    image = image.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    # Step 2: Convert the image to Tkinter-compatible PhotoImage
    photo = ImageTk.PhotoImage(image)
    
    # Step 3: Create a Label widget to display the image
    image_label = tk.Label(root, image=photo)
    image_label.image = photo  # Prevent garbage collection of the image
    image_label.pack(pady=20)
    
    # Step 4: Handle the second image
    image2 = Image.open('Shruti and me 2.jpg')
    image2 = image2.resize((target_width, target_height), Image.Resampling.LANCZOS)
    photo2 = ImageTk.PhotoImage(image2)
    
    # Create a Label widget for the second image
    image_label2 = tk.Label(root, image=photo2)
    image_label2.image = photo2  # Prevent garbage collection
    image_label2.pack(pady=20)
    
    # EXIT BUTTON SECTION
    exit_button = tk.Button(root, text="Exit", command=exit_app)
    exit_button.pack(pady=10)
    
    # Start the Tkinter event loop
    root.mainloop()
    return

if __name__ == "__main__":
    change_dir()
    main()