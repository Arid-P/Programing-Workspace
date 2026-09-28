import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("Image Viewer")

def change_dir() -> None:
    #tk.Label(root, text=os.getcwd(.pack()
    os.chdir("/storage/emulated/0/Programing/Python/GUI/Basics/Images") 
    #tk.Label(root, text=os.getcwd(.pack()
    return



images = []
img_idx = 0
length = 0
row_img = 2 


def resize_image(img: Image.Image, target_width: int = 784, target_height: int = 441) -> Image.Image:
    """
    Resize the given image proportionally to fit within the target dimensions.

    Args:
        img (Image.Image): The image to be resized.
        target_width (int): The target width for resizing.
        target_height (int): The target height for resizing.

    Returns:
        Image.Image: The resized image.
    """
    # Get original dimensions
    original_width, original_height = img.size

    # Calculate aspect ratio
    aspect_ratio = original_width / original_height

    # Adjust dimensions while maintaining aspect ratio
    if target_width / target_height > aspect_ratio:
        # Fit to height
        new_height = target_height
        new_width = int(new_height * aspect_ratio)
    else:
        # Fit to width
        new_width = target_width
        new_height = int(new_width / aspect_ratio)

    # Resize proportionally
    return img.resize((new_width, new_height), Image.Resampling.LANCZOS)



def load_img () -> None : 
    global images, length, img_lab, row_img, error_lab
    
    img_names: list = os.listdir()
    img_names = sorted(img_names)
    
    for name in img_names:
        try :
            img = Image.open(name)
            img = resize_image(img)
            images.append(ImageTk.PhotoImage(img))
        except Exception as e :
            error_lab = tk.Label(root, text = f"Skipping {name}:  {e}")
            error_lab.grid(row=row_img, column = 0)
            row_img += 1
    
    length = len(images)
    img_lab = tk.Label(root, image=images[img_idx])
    img_lab.grid(row=row_img,column=0, columnspan=3)
    show_status_bar()
    
    return


def show_status_bar () -> None:
    global img_idx, length
    #bd for border, relief to get that inside or 3d look and anchor for putting it to one side like alignment, E for east
    status_bar = tk.Label(root, text = f"Image {img_idx+1} of {length}.", bd =
    2, relief="sunken", anchor="e")
    #sticky is used to strecth the bd of the column. W is for west and E is for east
    status_bar.grid(row=1, column=0, columnspan=3, sticky="we")
    return


def show_img () -> None : 
    global img_idx, img_lab, error_lab
    error_lab.destroy()
    img_lab.destroy()
    
    img_lab = tk.Label(root, image=images[img_idx])
    img_lab.grid(row=2, column=0, columnspan=3)
    
    load_buttons()
    show_status_bar()
    return


def forward () -> None :
    global img_idx
    img_idx = (img_idx + 1) % length
    return show_img()


def backward () -> None :
    global img_idx
    img_idx = (img_idx - 1) % length
    return show_img()

def load_buttons () -> None :
    but_forward = tk.Button(root, text=">>", command = forward)
    but_exit = tk.Button(root, text="Exit Viewer", command = root.destroy)
    but_back = tk.Button(root, text="<<", command = backward)
    
    but_back.grid(row = 0, column = 0)
    but_exit.grid(row = 0, column = 1)
    but_forward.grid(row = 0, column = 2)
    
    return


def main () -> None :
    load_buttons()
    load_img()
    #show_img() 
    
    root.mainloop()
    return

if __name__ == "__main__" :
    change_dir()
    main()