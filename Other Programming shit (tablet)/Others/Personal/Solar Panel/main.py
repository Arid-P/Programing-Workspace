#Imports: {
#GUI imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import Toplevel

#Date imports
from datetime import datetime as dt
from datetime import date as d

#File imports
import os
from os import chdir
import sys
#}

#Start shit: {
#creting the main window
root = tk.Tk()
root.title("Solar Power Manager")
root.geometry("780x1200")


#Getting folder location
year = str(d.today().year)
month = str(d.today().strftime("%d %B").split(" ")[1])

folder_path = os.path.join("/storage/emulated/0/Documents/Balances/Solar", year)
file_path = os.path.join(folder_path, month)

paths = [folder_path, file_path]

#setting the style globally
style = ttk.Style()
#}


class LoadingData:
    """Docstring"""
    @staticmethod
    def load_data() -> None:
        """Docstring"""
        chdir(paths[0])
        
        all_data = []
        with open(f"{month}.txt", "r") as f :
            all_data.append(f.read())
        
        i = 2
        n = len(all_data)
        print(all_data)
        while i <= n :
            all_data.pop(i)
            i += 3
        
        #formatted_data = f"{data[0]}: {data[2]}, {data[3]}  ({data[1]})\n"
        #formatted_data = [/data[0]:/ /data[2],/ /data[3]/  /(data[1])/]
        fa_data = []
        for da in all_data :
            da = da.replace("\n", "").split(" ")
            t = [da[0].replace(":", ""), da[1].replace(",", ""), da[2], da[3].replace("(", "").replace(")", "")]
            fa_data.append(t)
        
        for k in fa_data :
            print(k)
        return



class SavingData ():
    @staticmethod
    def checking_and_initalising_file () -> None:
        """Docstring"""
        
        if not os.path.exists(paths[0]) :
            chdir("/storage/emulated/0/Documents/Balances/Solar/")
            os.mkdir(f"{year}")
            f =  open(f"{month}.txt", "a")
            f.close()
            
        elif not os.path.isfile(paths[1]) :
            f =  open(f"{month}.txt", "a")
            f.close()
        
        return
    
    
    @staticmethod
    def save_data(data) -> None:
        """Docstring"""
        formatted_data = f"{data[0]}: {data[2]}, {data[3]}  ({data[1]})\n" if data[1] == "Morning" else f"{data[0]}: {data[2]}, {data[3]} ({data[1]})\n\n"
        
        chdir(paths[0])
        with open(paths[1], "a") as f :
            f.write(formatted_data)
        
        return
    
    
    @staticmethod
    def collect_input() -> None:
        """Docstring"""
        global date_selector, day_time, spend, made
        data = [] #date, time, spend, made
        
        selected_date = date_selector.get_date()
        formatted_date = selected_date.strftime("%d %B")
        data.append(formatted_date)
        
        
        data.append(day_time.get())
        
        
        spend_amount = spend.get()
        made_amount = made.get()
        
        if spend_amount.strip() and made_amount.strip() :
            try :
                spend_amount = int(spend_amount)
                made_amount = int(made_amount)
            except Exception as e:
                messagebox.showerror("Error", f"Kindly Enter an whole number amount as the following error has occured \n {e}")
                return 
            
            if spend_amount > 0 and made_amount > 0:
                data.append(spend_amount)
                data.append(made_amount)
            else:
                messagebox.showwarning("Warning", "Kindly enter positive number amount")
                return
        else:
            messagebox.showwarning("Warning", "Kindly enter some amount")
            return
        
        SavingData.save_data(data)
        return 



class GUI :
    @staticmethod
    def styles () -> None :
        """ Creates all the Styles used in the code in it """
        style.configure("Custom.TFrame", font=("Arial", 11), anchor="w",
        borderwidth=3, relief="sunken", background="#d6d4d4") 
        
        style.layout("Custom.TButton", style.layout("TButton"))
        style.configure("Custom.TButton", font=("Arial", 13), relief="sunken")
        
        return
    
    
    @staticmethod
    def frames() -> None:
        global f_time, f_amount, f_extra
        f_time = ttk.LabelFrame(root, text="Selct Time", style="Custom.TFrame", padding=(5, 6, 5, 6))
        f_time.place(x=30, y=20, width=310)
        
        f_amount = ttk.LabelFrame(root, text="Enter Amount", style="Custom.TFrame", padding=(5, 6, 5, 6))
        f_amount.place(x=30, y=145, width=310)
        return
    
    
    @staticmethod
    def input_widgets () :
        """All the wigests used for input are inslaised here"""
        global date_selector, day_time, spend, made
        date_label = ttk.Label(f_time, text="Select a Date: ", font=("Arial", 12))
        date_label.grid(row=1, column=1)
        
        date_selector = DateEntry(f_time, date_pattern="dd/mm/yyyy", font=("Arial", 12))
        date_selector.grid(row=1, column=2, columnspan=3)
        
        ttk.Label(f_time, text="            ", font=("Arial", 5)).grid(row=2, column=0, columnspan=5)
        
        day_time = tk.StringVar(value="Morning")
        tk.Radiobutton(f_time, text="Morning", variable=day_time, value="Morning", font=("Arial", 12)).grid(row=3, column=1)
        tk.Radiobutton(f_time, text="Night", variable=day_time, value="Night", font=("Arial", 12)).grid(row=3, column=3)
        
        
        
        spend_label = ttk.Label(f_amount, text="Sepnd: ", font=("Arial", 12))
        spend_label.grid(row=1, column=1)
        spend = ttk.Entry(f_amount, font=("Arial", 12))
        spend.grid(row=1, column=3, columnspan=2)
        
        ttk.Label(f_amount, text="            ", font=("Arial", 6)).grid(row=2, column=0, columnspan=5)
        
        made_label = ttk.Label(f_amount, text="Made: ", font=("Arial", 12))
        made_label.grid(row=3, column=1)
        made = ttk.Entry(f_amount, font=("Arial", 12))
        made.grid(row=3, column=3, columnspan=2)
        
        
        ttk.Button(root, text="S\nU\nM\nB\nI\nT", style="Custom.TButton", command=SavingData.collect_input).place(x=350, y=27, width=50, height=229)
        return



def main () -> None :
    GUI.styles()
    GUI.frames()
    GUI.input_widgets()
    
    SavingData.checking_and_initalising_file()
    LoadingData.load_data()

    root.mainloop()
    return

if __name__ == "__main__" :
    main()
