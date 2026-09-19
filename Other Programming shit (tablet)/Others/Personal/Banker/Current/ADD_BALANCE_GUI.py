#GUI imports
#GUI imports
#GUI imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import Toplevel

#Date imports
from datetime import datetime as dt
from datetime import date as d

#File import
import os
import sys
import importlib.util


#Creating the main window
root = tk.Tk()
root.title("Banker")
root.geometry("790x1250")

#For availability of styles globally
style = ttk.Style()

year = str(d.today().year)



class FileImportsManage () :
    @staticmethod
    def change_directory() -> None:
        """
        Change the current working directory to the specified path.
        """
        os.chdir("/storage/emulated/0/Documents/Balances/Money")
        return
    
    
    @staticmethod
    def add_path_cwd() -> None:
        sys.path.append("/storage/emulated/0/Programing/Python/Banker/Current/")  # Add current directory to sys.path
        return



class InternalProcessing () :
    
    @staticmethod
    def initialize_balance_file() -> None:
        """
        Creates the 'balance 2025.txt' file if it doesn't exist. Asks the user for initial total 
        and piggy values, and writes them to the file. Non-integer values are set to 0.
        """
        lines: list[str] = []
        
        if not os.path.exists(f"balance {year}.txt"):
            print("File not found, So creating it")
            with open(f"balance {str(int(year) - 1) }.txt", "r") as file:
                lines = file.readlines()
            
            with open(f"balance {year}.txt", "w+") as file:
                file.write(lines[-2])
                file.write(lines[-1])
    
    @staticmethod
    def update_balance_file(data: list, updated_total: int) -> None:
        """
        Write new data to the file 'balance 2025.txt' including total values.
    
        Parameters:
        - data (list): Transaction details.
        - updated_total (int): Updated total value.
        """
        global extra_info
        
        raw = extra_info_in.get("1.0", tk.END).strip()
        formatted = raw.replace('\n', ' ')
        extra_info = f"({formatted})" 
        
        new_line = f"{data[0]} {data[1]} rs on {data[2]} {extra_info}\n"
        updated_amount = f"Total = {updated_total} rs."
    
        with open(f"balance {year}.txt", 'a') as file:
            file.write('\n\n')
            file.write(new_line)
            file.write(updated_amount)
    
    @staticmethod
    def process_transaction(data: list) -> None:
        """
        Extract current balance and update it based on transaction data.
    
        Parameters:
        - data (list): Transaction details.
        """
        #[Total] [[3132] [rs.]]
        with open(f"balance {year}.txt", 'r') as file:
            lines = file.readlines()
            last_line = lines[-1]
            total = int(last_line.split(" = ")[1].split(" ")[0])
    
        if data[0] == 'Gained':
            updated_total = total + data[1]
        else:
            updated_total = total - data[1]
    
        InternalProcessing.update_balance_file(data, updated_total)
    
    
    @staticmethod
    def collect_input() -> list:
        """
        Collect user input for transaction details.
    
        Returns:
        - list: Transaction data.
        """
        global transaction_data, s_or_g, custom_date
        transaction_data = []
        
        transaction_data.append(s_or_g.get())
        
        if amount.get().strip() :
            try :
                if int(amount.get().strip()) > 0:
                    transaction_data.append(int(amount.get().strip()))
                else:
                    messagebox.showwarning("Warning", "Kindly enter positive number amount")
                    return
            except Exception as e:
                messagebox.showerror("Error", f"Kindly Enter an whole number amount as the following error has occured \n {e}")
                return
        else:
            messagebox.showwarning("Warning", "Kindly enter some amount")
            return
        
        selected_date = custom_date.get_date()
        formatted_date = selected_date.strftime("%d %B")
        transaction_data.append(formatted_date)
        
        #ttk.Label(root, text=transaction_data, font=("Arial", 10)). place(x=300, y=500)
        
        InternalProcessing.process_transaction(transaction_data)
        
        GUI.frames(True)
        TransactionInfo.current_transaction()



class TransactionInfo (InternalProcessing) :
    @staticmethod
    def last_transaction(year_:str = year) -> None :
        """Function to print the last transaction stored in the file."""
        with open(f"balance {year_}.txt", "r") as file:
            lines = file.readlines()
            
            # The last two lines of the file contain the last transaction
            ttk.Label(last_frame, text=lines[-2].replace("\n", ""), font=("Arial", 10)).pack()
            ttk.Label(last_frame, text=lines[-1], font=("Arial", 10)).pack()
            #ttk.Label(last_frame, text="\n\n", font=("Arial", 8)).pack()
    
    @staticmethod
    def current_transaction(year_:str = year) -> None :
        """Function to print the last transaction stored in the file."""
        with open(f"balance {year_}.txt", "r") as file:
            lines = file.readlines()
            
            # The last two lines of the file contain the last transaction
            ttk.Label(curr_frame, text=lines[-2].replace("\n", ""), font=("Arial", 10)).pack()
            ttk.Label(curr_frame, text=lines[-1], font=("Arial", 10)).pack()
            #ttk.Label(last_frame, text="\n\n", font=("Arial", 8)).pack()
            
            #ttk.Label(curr_frame, text="", font=("Arial", 10)).pack()
    
    @staticmethod
    def all_transactions () -> None :
        with open(f"balance {year}.txt", "r") as f :
            transactions: list[str] = f.readlines()
        
        new_window = Toplevel(root)
        new_window.title("All transactions")
        new_window.geometry("650x1200")
    
        # Add a label to the new window
        label = tk.Label(new_window, text="".join(transactions))
        label.pack(pady=20)
    
        # Add a button to close the new window
        close_button = ttk.Button(new_window, text="Close", command=new_window.destroy)
        close_button.pack(pady=10)
    
    
    @staticmethod
    def get_year_input () -> None :
        response = tk.messagebox.askyesno("Choose Year", "Do you Want the previous year?")
        
        if response :
            TransactionInfo.show_max_min(str( int(year) - 1))
        else :
            new_window = Toplevel(root)
            new_window.title("Enter the Year")
            new_window.geometry("400x200")
            
            
            label = ttk.Label(new_window, font=("Arial", 12), text="Enter year: ")
            label.place(x=40, y=50)
            
            
            years = [str(y) for y in range(2023, int(year)+1) ]
            selected_year= tk.StringVar()
            selected_year.set(years[-2])  # Set the default value to the first option
            
            dropdown = ttk.Combobox(
                new_window,
                textvariable=selected_year, 
                values=years,  # List of options for the dropdown
                state="readonly"  # Making the dropdown read-only
            )
            dropdown.place(x=145, y=50, width=100)
            
            
            def click() :
                year_ = selected_year.get()
                new_window.quit()
                TransactionInfo.show_max_min(year_)
            
            style = ttk.Style()
            #First define the layput then defining the font
            style.layout("Custom.TEExitButton", style.layout("TButton"))
            style.configure("Custom.TEExitButton", font=("Arial", 13), anchor="center")  # Defining Exit button style
            
            ttk.Button(new_window, text="Exit", style="Custom.TEExitButton", command=click).place(x=160, y=130, width=60, height=50)
        
        return
    
    
    @staticmethod
    def show_max_min (year_: str) -> None :
        #First add the path
        FileImportsManage.add_path_cwd()
        
        module_name = "find_max_min_from_total"
        module_path = "/storage/emulated/0/Programing/Python/Banker/Current/find_max_min_from_total.py"
        
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        fmm = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(fmm)
        
        maxmin = fmm.main(year_)
        
        #Last changing back to balance file path
        FileImportsManage.change_directory()
        
        
        new_window = Toplevel(root)
        new_window.title(f"Max and Min amoumt in {year_}")
        new_window.geometry("400x200")
        
        
        style = ttk.Style()
        style.configure("Custom.TLabelframe.Label", font=("Arial", 12))
        
        frame = ttk.LabelFrame(new_window, text="Maximum and Minum Value" ,style="Custom.TLabelframe.Label")
        frame.place(x=20, y=25)
        
        
        label = ttk.Label(frame, font=("Arial", 12), text=f"Maximum money in the year {year_}: {maxmin[0]}\nMinimum money in the year {year_}:  {maxmin[1]}")
        label.pack(padx=5, pady=5)
        
        
        #First define the layput then defining the font
        style.layout("Custom.TExitButton", style.layout("TButton"))
        style.configure("Custom.TExitButton", font=("Arial", 12), anchor="center")  # Defining Exit button style
        
        ttk.Button(new_window, text="Exit", style="Custom.TExitButton",
        command=new_window.quit).place(x=160, y=130, width=50, height=40)



class GUI :
    @staticmethod
    def frames(check: bool) -> None:
        global last_frame, Input, curr_frame

        # Create a style for LabelFrame
        style = ttk.Style()
        style.configure("Custom.TLabelframe.Label", font=("Arial", 11))

        last_frame = ttk.LabelFrame(root, text="Last Transaction", style="Custom.TLabelframe", padding=(10, 10))
        last_frame.place(x=210, y=20)

        Input = ttk.LabelFrame(root, text="Input", style="Custom.TLabelframe", padding=(10, 10))
        Input.place(x=210, y=170, width=400)

        if check :
            curr_frame = ttk.LabelFrame(root, text="Input", style="Custom.TLabelframe", padding=(10, 10))
            curr_frame.place(x=210, y=580, width=400)
        else :
            return
    
    
    @staticmethod
    def Input_widgets_nodate () :
        global s_or_g, pig, amount, extra_info_in #spend or gained
        
        s_or_g = tk.StringVar(value="Spend")
        pig = tk.BooleanVar(value = True)
        
        
        ttk.Label(Input, text="Amount: ", font=("Arial", 10)).grid(row=0, column=0)
        amount = ttk.Entry(Input, font=("Arial", 10))
        amount.grid(row=0, column=1, columnspan=2)
        
        
        tk.Radiobutton(Input, text="Spend", variable=s_or_g, value="Spend", font=("Arial", 9)).grid(row=1, column=0)
        tk.Radiobutton(Input, text="Gained", variable=s_or_g, value="Gained", font=("Arial", 9)).grid(row=1, column=1)
        
        
        ttk.Label(Input, text="", font=("Arial", 10)).grid(row=2, column=0)
        
        
        GUI.set_date_widgets()
        
        ttk.Label(Input, text="", font=("Arial", 10)).grid(row=5, column=0)
        
        
        ttk.Label(Input, text="Extra Info: ", font=("Arial", 10)).grid(row=6, column=0)
        
        extra_info_in = tk.Text(Input, height=4, width=25, font=("Arial", 10), wrap="word")
        extra_info_in.grid(row=6, column=1, columnspan=2)     
        
        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 10)) 

        ttk.Button(Input, text="Submit", style="Custom.TButton", command=InternalProcessing.collect_input).grid(row=11, column=1)
    
    
    @staticmethod
    def set_date_widgets () -> None :
        global date, label_custom, custom_date, r
        r = 9
        
        label_custom = ttk.Label(Input, text="Select a Date", font=("Arial",
        10)).grid(row=3, column=0, columnspan = 2)
        
        custom_date = DateEntry(Input, date_pattern="dd/mm/yyyy", font=("Arial",
        10))
        custom_date.grid(row=4, column=0, columnspan = 2)
        
        ttk.Label(Input, text="", font=("Arial", 10)).grid(row=10, column=0)
        
        return
    
    
    @staticmethod
    def feature_buttons () -> None : 
        ttk.Button(root, text="Exit", style="Custom.TExitButton", command=root.quit).place(x=30, y=15, width=90, height=50)
        
        ttk.Button(root, text="All Tran-\nsaction", style="Custom.TTransactionButton", command=TransactionInfo.all_transactions).place(x=30, y=90, width=90, height=70)
        
        ttk.Button(root, text="Min/Max \nTrans-\naction", style="Custom.TMin&MaxButton", command=TransactionInfo.get_year_input).place(x=30, y=190, width=90, height=80)
        
        return
    
    
    @staticmethod
    def styles () -> None :
        # First define the layput then defining the font
        style.layout("Custom.TExitButton", style.layout("TButton"))
        style.configure("Custom.TExitButton", font=("Arial", 13), anchor="center")  # Defining Exit button style
        
        
        style.layout("Custom.TTransactionButton", style.layout("TButton"))
        style.configure("Custom.TTransactionButton", font=("Arial", 11), anchor="center", padding=(5,0))  # Defining All Transaction button style
        
        
        style.layout("Custom.TMin&MaxButton", style.layout("TButton"))
        style.configure("Custom.TMin&MaxButton", font=("Arial", 10), anchor="center", padding=(5,0))  # Defining All Transaction button style
        
        GUI.feature_buttons()
        return



def main() -> None:
    """
    Main function to execute the program.
    """
    global transaction_data


    GUI.styles()
    GUI.frames(False)
    GUI.Input_widgets_nodate()
    #GUI.set_date_widgets() is done in Input_widgets_ndate
    
    FileImportsManage.change_directory()
    InternalProcessing.initialize_balance_file()
    
    TransactionInfo.last_transaction()
    
    #InternalProcessing.collect_input() is called in the submit button
    root.mainloop()

if __name__ == "__main__":
    main()

