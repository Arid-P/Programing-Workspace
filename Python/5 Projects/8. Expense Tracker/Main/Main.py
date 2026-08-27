#Libraries for GUi
import tkinter as tk
from tkinter import ttk
from tkinter import Canvas

#Libraries for files
import sys
import os
#for debugging
import inspect


#creting the main window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("750x40+10+40")

#Force the window to update its size
root.update_idletasks()


#setting the style globally
style = ttk.Style()


class Debug () :
    def d(*args):
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


class LoadData () :
    
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


class Utils () :
    
    @staticmethod
    def styles () -> None :
        """ Cretes all the Styles used in the code in it """
        
        style.configure("Add.TButton", font=("Arial", 18), foreground="blue", background="grey", padding=(5, -3, 5, 8))
        style.configure("Exit.TButton", font=("Arial", 12), foreground="black")
        style.configure("Categories.TMenubutton", font=("Arial", 12), pady=-2)
        
        style.configure("Custom.Treeview", rowheight=50)  
    
    
    @staticmethod
    def display_table(data: list[list[str]], filter_table_call: bool= False, first_call: bool = False) -> None:
        # Define column names
        columns = ("Date", "Amount", "Description", "Category")
        
        # Create Treeview widget (table)
        table = ttk.Treeview(root, columns=columns, show="headings", style="Custom.Treeview")
        # 'columns' parameter defines the columns in the table
        # 'show="headings"' hides the default first empty column
        
        # Define column headings
        for col in columns:
            table.heading(col, text=col)  # Sets the column title in the header
            table.column(col, width=100)  # Sets the width of the column
        
        if not data :
            data =[ ("None", "None", "None", "None") ]
        else :
            total_amount = 0
            for d in data :
                total_amount += int(d[1])
            
            total_expense = ("", total_amount, "Total amount", "") 
            data.append(total_expense)
        
        
        for expense in data:
            table.insert("", "end", values=expense)
            # The first argument "" means the row is added at the root level (no parent)
            # The second argument "end" adds the row at the last position
            # The 'values' parameter specifies the content for the row


        #Increasing the window size then diaplaying the table
        curr_height_root = int(root.geometry().split("+")[0].split("x")[1])
        
        if first_call :
            new_height_root = curr_height_root + (50 * (len(data) + 1) )
        else :
            new_height_root = curr_height_root + 50 
        
        root.geometry(f"770x{new_height_root}")
        #Force the window to update its size
        root.update_idletasks()
        
        global main_table_height
        table_height: int = (50 * ( len(data) + 0.55) )
        
        table.place(relx=0, rely=0, relwidth=1, height=table_height )
        main_table_height = table_height
        
        return
    
    
    @staticmethod
    def display_filter_table(data: list[list[str]], previous_data: list[list[str]], first_call: bool) -> None:
        # Define column names
        columns = ("Date", "Amount", "Description", "Category")
        
        # Create Treeview widget (table)
        table = ttk.Treeview(root, columns=columns, show="headings", style="Custom.Treeview")
        # 'columns' parameter defines the columns in the table
        # 'show="headings"' hides the default first empty column
        
        # Define column headings
        for col in columns:
            table.heading(col, text=col)  # Sets the column title in the header
            table.column(col, width=100)  # Sets the width of the column
        
        
        for expense in data:
            table.insert("", "end", values=expense)
            # The first argument "" means the row is added at the root level (no parent)
            # The second argument "end" adds the row at the last position
            # The 'values' parameter specifies the content for the row


        #Increasing the window size then diaplaying the table
        curr_height_root = int(root.geometry().split("+")[0].split("x")[1])
        change_in_data = len(data) - len(previous_data) 
        
        if first_call :
            curr_height_root += 50 #For label 
            new_height_root = curr_height_root + ( 50 * (len(data) +1))#For table 
            table_height: int = (50 * -1 * (len(data) + 0.55) )
        
        else :
            if len(data) > len(previous_data) :
                new_height_root = curr_height_root + ( 50 * change_in_data)  #For table 
                table_height: int = (50 * (change_in_data + 0.55) )
            
            elif len(data) < len(previous_data) : 
                new_height_root = curr_height_root - ( 50 * -1 * change_in_data ) #For table 
                table_height: int = (50 * -1 * (change_in_data + 0.55) )
            else :
                new_height_root = curr_height_root
                table_height: int = (50 * 0.55)
            
        
        root.geometry(f"770x{new_height_root}")
        #Force the window to update its size
        root.update_idletasks()
        
        global main_table_height, previous_table
        
        if change_in_data > 0 : 
            table.place(relx=0, y=(main_table_height + 70), relwidth=1, height=table_height)
        elif change_in_data < 0: 
            previous_table.place_forget()
        
        previous_table = table
        return
    
    
    @staticmethod
    def filter_data (selected_category, first_call: bool=False) -> None :
        expenses = LoadData.load_expenses()
        
        filtered_epenses = []
        for expense in expenses :
            expense_category = expense[-1]
            if expense_category == selected_category :
                filtered_epenses.append(expense)
        
        global previous_expenses
        previous_data = previous_expenses
        previous_expenses = filtered_epenses
        
        return Utils.display_filter_table(filtered_epenses, previous_data, first_call)



def main () -> None :
    """ Sets up all the main widegts and then perform other tasks in sequence"""
    
    global main_table_height, previous_expenses #used in display_table and display_filter_table
    previous_expenses = []
    
    
    Utils.styles() #setting up the styles
    FileImports.change_dir() # changing to appropriate directory
    
    Utils.display_table(LoadData.load_expenses(), first_call=True)
    Utils.filter_data("Nothing", first_call=True)
    
    
    
    #Filter Table code
    fil_label = ttk.Label(root, text="Select Category: ", font=("Arial", 13))
    fil_label.place(relx=0, rely=1, anchor="sw", x=10, y=-10)
    
    categories = LoadData.load_categories()
    
    selected_category = tk.StringVar()
    selected_category.set(categories[0])  # Default value
    
    # Creating dropdown menu
    dropdown = ttk.OptionMenu(root, selected_category, *categories, command=Utils.filter_data, style="Categories.TMenubutton")
    dropdown.place(relx=0, rely=1, anchor="sw", x=180, y=-10, width=240, height=30)
    
    filter_tab_label= tk.Label(root, text="Selected Category's Table: ", font=("Arial", 13))
    filter_tab_label.place(x=10, y=(main_table_height + 30))
    
    
     
    #Main table code
    def add_expense () -> None :
        FileImports.add_path_cwd()
        import addexpense as ae
        new_window = ae.main(root)
        
        root.wait_window(new_window) #stops execution untill the cureent window is closed
        FileImports.change_dir() # changing back
        
        Utils.display_table(LoadData.load_expenses())
        filter_tab_label.place_forget()
        filter_tab_label.place(x=10, y=(main_table_height + 30))
        return
    
    add_button = ttk.Button(root, text="+", style="Add.TButton", command=add_expense)
    add_button.place(relx=1, rely=1, anchor="se", x=-10, y=-10, width =45, height=40) # Negative x and y for padding
    
    
    exit_button = ttk.Button(root, text="Exit", style="Exit.TButton", command=add_expense)
    exit_button.place(relx=1, rely=1, anchor="se", x=-70, y=-10, width =45, height=40) # Negative x and y for padding
    
    
    root.mainloop()
    return



if __name__ == "__main__" :
    main()