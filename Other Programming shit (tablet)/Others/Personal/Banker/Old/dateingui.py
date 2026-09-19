import tkinter as tk
from tkinter import messagebox
from datetime import datetime as dt
from tkcalendar import DateEntry


class DateInputApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Date Input Example")
        self.root.geometry("600x400")

        # Variable to store the user's choice
        self.want_curr_date = tk.BooleanVar(value=False)

        # UI Components
        self.create_widgets()

    def create_widgets(self):
        """Create and place all widgets in the app."""
        # Labels and Radiobuttons
        tk.Label(self.root, text="Want the Current Date?", font=("Arial", 12)).place(x=200, y=20)
        tk.Radiobutton(self.root, text="Yes", variable=self.want_curr_date, value=True, font=("Arial", 12),
                       command=self.forget_place).place(x=200, y=60)
        tk.Radiobutton(self.root, text="No", variable=self.want_curr_date, value=False, font=("Arial", 12),
                       command=self.get_place).place(x=280, y=60)

        # DateEntry widget (hidden by default)
        self.label_cus_date = tk.Label(self.root, text="Select a Date", font=("Arial", 12))
        self.label_cus_date.place_forget()

        self.custom_date = DateEntry(self.root, date_pattern="dd/mm/yyyy", font=("Arial", 10))
        self.custom_date.place_forget()

        # Submit button
        tk.Button(self.root, text="Submit", font=("Arial", 12), command=self.handle_submit).place(x=240, y=220)

        # Exit button
        tk.Button(self.root, text="Exit", font=("Arial", 12), command=self.root.quit).place(x=260, y=270)

    def forget_place(self):
        """Hide the custom date selection widgets."""
        self.label_cus_date.place_forget()
        self.custom_date.place_forget()

    def get_place(self):
        """Show the custom date selection widgets."""
        self.label_cus_date.place(x=200, y=120)
        self.custom_date.place(x=200, y=160)

    def handle_submit(self):
        """Handle the submit action based on the user's selection."""
        if self.want_curr_date.get():
            date = dt.today().strftime("%d-%B")  # Get current date in "01-January" format
        else:
            selected_date = self.custom_date.get_date()  # Get date as a `datetime.date` object
            date = selected_date.strftime("%d-%B")  # Format as "01-January"
        self.submit_dates(date)

    @staticmethod
    def submit_dates(date):
        """Display the selected or current date."""
        try:
            messagebox.showinfo("Date Entered", f"The selected date is: {date}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


def main():
    root = tk.Tk()
    DateInputApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()