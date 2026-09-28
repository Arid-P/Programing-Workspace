import tkinter as tk
from tkinter import ttk, Toplevel
import os

def change_dir() -> None:
    os.chdir("/storage/emulated/0/Programing/Python/Projects/7. To Do List App/Main Code")

def add_task(new, entry_widget) -> None:
    """ Saves new task and closes the window """
    task_title = entry_widget.get().strip()
    
    if task_title:
        try:
            with open("Tasks.txt", "r") as f:
                tasks = [task.strip() for task in f.readlines() if task.strip()]
        except FileNotFoundError:
            tasks = []

        tasks.append(task_title)

        with open("Tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")
    
    new.destroy()  # Close window after saving


def create_task_window(parent) -> None:
    """ Creates the task entry window """
    change_dir()

    new = Toplevel(parent)  
    new.title("Add Task")
    new.geometry("400x400")

    entry_widget = ttk.Entry(new, width=20, font=("Arial", 14))
    entry_widget.place(x=50, y=30)

    submit_button = ttk.Button(new, text="Submit", command=lambda: add_task(new, entry_widget))
    submit_button.place(x=115, y=90)
    
    return new
    