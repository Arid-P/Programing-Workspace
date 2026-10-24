# Import necessary modules from tkinter

import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Tkinter Message Box Example")

#Message box is used to dispaly a message
#syntax: messagebox.itstype("Title", "Message") 
#message box are of various types so yoy have to use them accordin to the use case

# Function to display an info message box
def show_info():
    messagebox.showinfo("Information", "This is an info message.")

# Function to display a warning message box
def show_warning():
    messagebox.showwarning("Warning", "This is a warning message.")

# Function to display an error message box
def show_error():
    messagebox.showerror("Error", "This is an error message.")

# Function to ask a question and print the response
#returns yes or no
def ask_question():
    response = messagebox.askquestion("Question", "Do you like Python?")
    print(f"Response: {response}")
    tk.Label(root, text = f"Response: {response}").pack()

# Function to ask for confirmation and print the response
#returns true or false
def ask_ok_cancel():
    response = messagebox.askokcancel("Confirm", "Do you want to proceed?")
    print(f"Response: {response}")
    tk.Label(root, text = f"Response: {response}").pack()

# Function to ask a yes/no question and print the response
#returns true or false
def ask_yes_no():
    response = messagebox.askyesno("Choose", "Do you agree?")
    print(f"Response: {response}")
    tk.Label(root, text = f"Response: {response}").pack()

# Create buttons to trigger each message box
btn_info = tk.Button(root, text="Show Info", command=show_info)
btn_warning = tk.Button(root, text="Show Warning", command=show_warning)
btn_error = tk.Button(root, text="Show Error", command=show_error)
btn_question = tk.Button(root, text="Ask Question", command=ask_question)
btn_ok_cancel = tk.Button(root, text="Ask OK/Cancel", command=ask_ok_cancel)
btn_yes_no = tk.Button(root, text="Ask Yes/No", command=ask_yes_no)

# Pack the buttons into the window
btn_info.pack(pady=5)
btn_warning.pack(pady=5)
btn_error.pack(pady=5)
btn_question.pack(pady=5)
btn_ok_cancel.pack(pady=5)
btn_yes_no.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()