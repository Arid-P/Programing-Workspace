# Notes on ttk and Styling in Tkinter

# Introduction to ttk
# The `ttk` module (Themed Tkinter) is an extension of the standard `tkinter` module in Python, providing modern and visually appealing widgets.
# It allows for better styling and theming of GUI applications.

# Importing ttk
import tkinter as tk
from tkinter import ttk

# Basic ttk Widgets
# The `ttk` module provides various widgets similar to `tkinter`, but with improved aesthetics:
# - `ttk.Button`
# - `ttk.Label`
# - `ttk.Entry`
# - `ttk.Frame`
# - `ttk.Combobox`
# - `ttk.Checkbutton`
# - `ttk.Radiobutton`
# - `ttk.Progressbar`
# - `ttk.Treeview`
# - `ttk.Notebook`

# Example of creating a simple `ttk` button
root = tk.Tk()
button = ttk.Button(root, text="Click Me")
button.pack(pady=10)
root.mainloop()

# Styling ttk Widgets
# The `ttk.Style()` class allows customization of the appearance of widgets.

# Creating a Style Object
style = ttk.Style()

# Setting a Theme
# Tkinter provides built-in themes that can be used:
style.theme_use("clam")  # Other themes: 'default', 'alt', 'classic', 'vista', 'xpnative'

# Configuring Widget Styles
# Each `ttk` widget has a style that can be customized. Styles are identified by `widget class` names.

# Changing a Button Style
style.configure("TButton", font=("Arial", 12, "bold"), foreground="blue", background="lightgrey")

# Creating a Custom Style
# You can create a custom style by giving it a unique name:
style.configure("My.TButton", font=("Arial", 14), foreground="white", background="blue", padding=10)
button = ttk.Button(root, text="Styled Button", style="My.TButton")
button.pack(pady=10)

# Modifying a Label Style
style.configure("TLabel", font=("Arial", 12), foreground="green")

# Styling States
# You can also define styles for different widget states such as `active`, `disabled`, etc.:
style.map("TButton", foreground=[("pressed", "red"), ("disabled", "grey")], background=[("active", "yellow")])

# Example Program with Styling
root = tk.Tk()
root.title("Styled ttk Widgets")

style = ttk.Style()
style.theme_use("clam")
style.configure("My.TButton", font=("Arial", 14), foreground="white", background="blue", padding=10)
style.configure("My.TLabel", font=("Arial", 12), foreground="green")

label = ttk.Label(root, text="Hello, ttk!", style="My.TLabel")
label.pack(pady=10)

button = ttk.Button(root, text="Click Me", style="My.TButton")
button.pack(pady=10)

root.mainloop()

# Summary
# - `ttk` provides improved widgets with better styling options.
# - `ttk.Style()` is used for theming and customization.
# - Styles can be applied to various widget states.
# - Custom styles can be defined and applied using a unique style name.

# By mastering `ttk` and its styling options, you can create professional-looking Tkinter applications with ease!

