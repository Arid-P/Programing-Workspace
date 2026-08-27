import tk as tk
from tk import Toplevel, ttk
from copy import deepcopy


import sys
import os

# Add directory to path
def add_path_cwd() -> None:
    sys.path.append("/storage/emulated/0/Programing/Python/Projects/7. To Do List App/Main Code/")

# Changes path to desired location
def change_dir() -> None:
    os.chdir("/storage/emulated/0/Programing/Python/Projects/7. To Do List App/Main Code/") 
    return

if __name__ == "__main__":
    add_path_cwd()
    import addingtask as at  # Import after modifying sys.path
    change_dir()




root = tk.Tk()
root.geometry("600x600")


# Create style instance
style = ttk.Style()

# Define custom styles
style.configure("Custom.TCheckbutton", font=("Arial", 10))  # Checkbutton font
style.configure("Custom.TButton", font=("Arial", 12, "bold"))  # Button font

class Widgets () :
    @staticmethod
    def frame ():
        global tasks_frame
        tasks_frame = tk.LabelFrame(root, text="Tasks", padx=10, pady=10)
        tasks_frame.place(x=15, y=20)
    
    
    @staticmethod
    def labels ():
        global textbox, tasks_frame
        if not load_uncomp_task() :
            textbox = ttk.Label(tasks_frame, text="No tasks yet", font=("Arial", 10))
            textbox.pack()
    
    
    @staticmethod
    def buttons ():
        Add_task_button = ttk.Button(root, text="+", style="Custom.TButton", command=add_task)
        Add_task_button.place(x=430, y=500)


def comp_task (task, tasks) -> None:
    tasks.remove(task)
    
    with open("Tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    
    print_task(tasks)


def print_task(tasks) -> None:
    """ Updates label with tasks """
    for widget in tasks_frame.winfo_children():
        widget.destroy()
    
    vars_ = [tk.IntVar() for _ in tasks]
    
    for idx, task in enumerate(tasks) :
        ttk.Checkbutton(tasks_frame, text=task, style="Custom.TCheckbutton", 
            command=lambda t=task: comp_task(t, tasks), 
                variable=vars_[idx]).pack(pady=5, anchor="w")


def load_uncomp_task() -> None:
    """ Loads tasks from file and updates display """
    with open("Tasks.txt", "r") as f:
        tasks = [task.strip() for task in f.readlines() if task.strip()]
    
    return tasks


def add_task() -> None:
    """ Opens the 'Add Task' window and updates task list """
    new_window = at.create_task_window(root)  
    root.wait_window(new_window) #stops execution untill the cureent window is closed
    root.after(5, lambda: print_task(load_uncomp_task()) )  


def main() -> None:
    """ Initializes the main Tkinter window """
    #Setting up the widgets
    Widgets.frame()
    Widgets.labels() 
    Widgets.buttons()
    
    tasks = load_uncomp_task()  # Load tasks when app starts
    print_task(tasks)  # Update the display
    
    root.mainloop()

if __name__ == "__main__":
    main()