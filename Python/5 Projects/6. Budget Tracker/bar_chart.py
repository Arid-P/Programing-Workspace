import matplotlib.pyplot as plt

def show_bar_chart(expenses):
    # Data for the bar chart
    categories = list(expenses.keys()).pop(-1)
    expenses_amount = list(expenses.values()).pop(-1)

    # Create the bar chart
    plt.bar(categories, expenses_amount, color='blue')

    # Add title and labels
    plt.title('Monthly Expenses Breakdown')
    plt.xlabel('Categories')
    plt.ylabel('Amount ($)')
    
    # Display the chart
    plt.show()

def main () -> None :
    # Call the function to display the chart
    show_bar_chart()
    return

if __name__ == "__main__" :
    main()
