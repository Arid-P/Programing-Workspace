import sys
import time as t
import matplotlib.pyplot as plt

def show_bar_chart(expenses):
    # Data for the bar chart
    categories = list(expenses.keys())[:-1]
    expenses_amount = list(expenses.values())[:-1]

    # Create the bar chart
    plt.bar(categories, expenses_amount, color='blue')

    # Add title and labels
    plt.title('Monthly Expenses Breakdown')
    plt.xlabel('Categories')
    plt.ylabel('Amount ($)')
    
    # Display the chart
    plt.show()



def take_input (type_: str = "in") -> dict[str, int] :
    source: dict[str, int] = {}
    
    source_text = "Enter the income source's name:  " if type_ == "in" else "Enter the expense source's name:  "
    
    amount_text = "Enter the amount earned from {}:  " if type_ == "in" else "Enter the amount spend from {}:  "
    
    total = 0
    
    while True :
        name = input(source_text) 
        if name in ["", "f", "fin"] :
            break
        
        while True :
            amount = input(amount_text.format(name)) 
            try :
                amount = int(amount) 
                if amount >= 0 :
                    break
                else:
                    print("Enter a positive integral value\n")
                    continue
            except ValueError :
                print("Enter a valid integral value\n")
        
        source[name] = amount
        total += amount
        print()
    
    source["Total"] = total
    return source



def main () -> None :
    #raise ValueError('main not implemented')
    
    print("Kindly enter your income source and the amount from it one by one")
    print("And once your are finished typing then press enter.\n")
    incomes = take_input()
    
    print("\n\nKindly enter your income source and the amount from it one by one")
    print("And once your are finished typing then press enter.\n")
    expenses = take_input("expense")
    
    #print(incomes, expenses, sep="\n\n\n")
    
    if expenses["Total"] > incomes["Total"] :
        print("Your expenses are more than your income so kindly reduce them, then enter the info again")
        return
    
    remaining_balance = incomes["Total"] - expenses["Total"]
    
    print(f"You save {remaining_balance} monthly and {remaining_balance * 12} yearly")
    
    t.sleep(10)
    
    show_bar_chart(expenses)
    return


if __name__ == "__main__" :
    main()