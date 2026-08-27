#Gui Libraries
import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from tkinter import messagebox

#Date Libraries
from datetime import datetime as dt

#File Libraries
import os
import sys

#for debugging
import inspect

class Debug () :
    def debug(*args):
        frame = inspect.currentframe().f_back  # Get caller's frame
        local_vars = frame.f_locals  # Get local variables in the function's scope
        
        output = []
        for arg in args:
            name = next((var for var, val in local_vars.items() if val is arg), "?")
            output.append(f"{name} = {repr(arg)}")  
    
        print(", ".join(output))  # Print formatted output
    


class FileImports () :
    def add_path_cwd() -> None:
        sys.path.append("/storage/emulated/0/Programing/Python/Projects/8. Expense Tracker/Main")  # Add current directory to sys.path
        return
    
    
    def change_dir() -> None:
        os.chdir("/storage/emulated/0/Programing/Python/Projects/8. Expense Tracker/Main")
        return
    


class DropdownMenu () :
    @staticmethod
    def add_option(widgets: list) -> None: # widgets = [new_categ_in, new_categ_lab, add_button]
        """Adds a new option to the dropdown menu."""
        #widgets: list = [new_categ_in, new_categ_lab, add_button]
        
        global categories, dropdown, selected_category
        new_option = widgets[0].get()
        
        if new_option and new_option not in categories:  # Avoid duplicates
            categories.insert(-1, new_option)
            
            menu = dropdown["menu"]
            menu.delete(0, "end")  # Clear current menu
            for category in categories:
                menu.add_command(label=category, command=lambda value=category: DropdownMenu.on_select(value))
            
            selected_category.set(categories[-2])
            
            widgets[0].delete(0, tk.END)  # Clear input field
            
            submit_button.config(state="enabled")
            
            for wid in widgets :
                wid.place_forget()
    
    
    @staticmethod
    def on_select (value) -> None :
        # Entry to add new option
        global categories, submit_button
        if value == categories[-1] : #something like value == "New Category"
            new_categ_lab = ttk.Label(new, font=("Arial", 9), text="New Category: ")
            new_categ_lab.place(x=80, y=200)
            
            new_categ_in = ttk.Entry(new, font=("Arial", 9))
            new_categ_in.place(x=190, y=200, width=80)
            
            submit_button.config(state="disabled")
            
            # Button to add new option
            add_button = ttk.Button(new, text="Add Option", style="Add_option.TButton", command=lambda:DropdownMenu.add_option([new_categ_in,
            new_categ_lab, add_button]))
            add_button.place(x=125, y=235, width=80, height = 30)
    


class Utils () :
    
    @staticmethod
    def styles () -> None :
        """ Cretes all the Styles used in the code in it """
        global style
        
        style.configure("Add_option.TButton", font=("Arial", 10), foreground="black", background="white", padding=2)
        
        style.configure("Submit.TButton", font=("Arial", 14), foreground="black", background="white", anchor="center", padding=(5, 0, 5, 0))
    
    
    @staticmethod
    def load_categories () -> list :
        categories = ""
        
        with open("Expenses.txt", "r") as f :
            line = str(f.readline())
            
            if line.endswith("\n") :
                line = line[0 : len(line)-1]
            
            categories = list(line.split("< "))
            
        return categories
    
    
    @staticmethod
    def load_expenses () -> list :
        
        with open("Expenses.txt", "r") as f :
            lines = f.readlines()
            lines.pop(0)
            
            if not lines :
                return []
            
            expenses = []
            for line in lines :
                if line.endswith("\n") :
                    line = line.replace("\n", "").split("< ")
                    expenses.append(line)
                else :
                    line = line.split("< ") 
                    expenses.append(line)
                   
            return expenses
    
    
    @staticmethod
    def input_not_valid (amount_wid) -> bool :
        value = amount_wid.get()
        
        try :
            value = int(value)
            if value <= 0 :
                messagebox.showwarning("Warning", "Kindly enter positive number amount")
                return True
        except ValueError :
            messagebox.showerror("Error", "Kindly Enter an whole number amount as the ValueError error has occured")
            return True
        
        return False
    
    
    @staticmethod
    def submit (info, amount_wid, desip_wid, selected_category) -> None :
        global categories
        total_expenses = Utils.load_expenses()
        
        if Utils.input_not_valid(amount_wid) :
            return
        
        info.append( amount_wid.get() )
        info.append( desip_wid.get() )
        info.append( selected_category.get() )
        
        total_expenses.append(info)
        
        with open("Expenses.txt", "w") as f :
            for category in categories :
                f.write(f"{category}")
                if category != categories[-1] :
                    f.write("< ")
            
            for expenses in total_expenses :
                f.write("\n")
                for expense in expenses :
                    f.write(f"{expense}")
                    if expense != expenses[-1] :
                        f.write("< ")
        
        
        return new.destroy()
    


def main (root) -> None :
    #creting another window for adding expense
    global new
    new = Toplevel(root)
    new.title("Enter Expense detail")
    new.geometry("500x400")
    
    
    #setting the style globally
    global style
    style = ttk.Style()
    Utils.styles()
    
    FileImports.change_dir()
    
    #Info need [Date, Amount, Description, Category]
    info: list = [dt.now().strftime("%d %B")]


    amount_lab = ttk.Label(new, font=("Arial", 12), text="Amount: ")
    amount_lab.place(x=40, y=25)
    
    amount_wid = ttk.Entry(new, width=20, font=("Arial", 12))
    amount_wid.place(x=120, y=25, width=175, height=35)


    desip_lab = ttk.Label(new, font=("Arial", 12), text="Description: ")
    desip_lab.place(x=40, y=90)
    
    desip_wid = ttk.Entry(new, width=20, font=("Arial", 12))
    desip_wid.place(x=150, y=90, width=175, height=35)


    categ_lab = ttk.Label(new, font=("Arial", 12), text="Select Category: ")
    categ_lab.place(x=40, y=160)
    
    # Predefined Categories
    global categories, selected_category
    categories = Utils.load_categories()
    selected_category = tk.StringVar()
    selected_category.set(categories[0])  # Default value
    
    # Create dropdown menu
    global dropdown
    dropdown = ttk.OptionMenu(new, selected_category, *categories, command=DropdownMenu.on_select)
    dropdown.place(x=200, y=160, width=100)


    global submit_button
    submit_button = ttk.Button(new, text="Submit", style="Submit.TButton", command=lambda :Utils.submit(info, amount_wid, desip_wid, selected_category))
    submit_button.place(x=110, y=270, width=250, height=40)
    
    
    return new


if __name__ == "__main__" :
    root = tk.Tk()
    root.title("Expense Tracker")
    root.geometry("1x1")
    main(root)
    root.mainloop()