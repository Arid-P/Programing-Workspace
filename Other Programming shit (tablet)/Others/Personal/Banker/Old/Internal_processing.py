from datetime import datetime as dt
from datetime import date as d
import os

year = str(d.today().year + 1)

class Internal_processing () :
    @staticmethod
    def change_directory() -> None:
        """
        Change the current working directory to the specified path.
        """
        os.chdir("/storage/emulated/0/Documents (genral & personal)/Balances")
    
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
    def print_last_transaction(year_:str = year):
        """Function to print the last transaction stored in the file."""
        with open(f"balance {year_}.txt", "r") as file:
            lines = file.readlines()
            
            if len(lines) > 0:
                # The last two lines of the file contain the last transaction
                print("\nLast transaction details: \n")
                print(lines[-2], lines[-1])
                print("\n\n")
            else:
                print("No transactions found.")
    
    @staticmethod
    def update_balance_file(data: list, updated_piggy: int, updated_total: int) -> None:
        """
        Write new data to the file 'balance 2025.txt' including updated piggy and total values.
    
        Parameters:
        - data (list): Transaction details.
        - updated_piggy (int): Updated piggy value.
        - updated_total (int): Updated total value.
        """
        extra_info = input('Do you want to input any extra info: ').strip().lower()
        extra_info = f"({extra_info})" if extra_info not in ['', 'no'] else ''
        new_line = f"{data[0]} {data[1]} rs on {data[2]} {extra_info}\n"
        updated_amount = f"Total = {updated_total} rs.   Piggy = {updated_piggy} rs"
    
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
        with open(f"balance {year}.txt", 'r') as file:
            lines = file.readlines()
            last_line = lines[-1] if lines else ''
            total = int(last_line.split('Total =')[-1].split('Piggy')[0].strip().replace('rs.', ''))
            piggy = int(last_line.split('Piggy =')[-1].strip().replace('rs', ''))
    
        if data[0] == 'Gained':
            updated_total = total + data[1]
            updated_piggy = piggy + data[1] if data[3] else piggy
        else:
            updated_total = total - data[1]
            updated_piggy = piggy - data[1] if data[3] else piggy
    
        Internal_processing.update_balance_file(data, updated_piggy, updated_total)
    
    @staticmethod
    def collect_custom_date() -> str:
        """
        Prompt the user to enter a custom date.
    
        Returns:
        - str: Custom date in "dd Month" format.
        """
        no_change = input('Do you want the date or month to remain the same? ').strip().lower()
        if no_change in [ 'n', 'no']:
            return input('Enter date: ')
        else:
            print()
    
        current_date_list = dt.now().strftime("%d %B").split()
        
        if input('Do you want the same month? ').strip().lower() in ['n', 'no']:
            current_date_list[1] = input('Enter month: ')
            return ' '.join(current_date_list)
        print()
        
        current_date_list[0] = input("Enter the date: ")
            
        # Converting this list into a string, then converting this string into a datetime object, and finally formatting it  
        return ' '.join(current_date_list)
    
    @staticmethod
    def collect_input() -> list:
        """
        Collect user input for transaction details.
    
        Returns:
        - list: Transaction data.
        """
        data = []
        transaction_type = input('Type s for spend and g for gained: ').strip().lower()
        if transaction_type in ['s', 'spend']:
            data.append('Spend')
        elif transaction_type in ['g', 'gained']:
            data.append('Gained')
        else:
            print()
            return Internal_processing.collect_input()
    
        print()
        while True: 
            try:
                data.append(int(input('Enter the amount: ')))
                break
            except ValueError:
                print('Enter a valid value')
                continue
    
        print()
        if input('Do you want the current date (y or yes)? ').strip().lower() in ['y', 'yes']:
            data.append(dt.now().strftime("%d %B"))
            print()
        else:
            data.append(Internal_processing.collect_custom_date())
    
        data.append(input('Piggy (type p for yes): ').strip().lower() in ['p', 'y', 'yes'])
        print()
        return data