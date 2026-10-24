from collections import namedtuple

def get_bonus_employees(employees: list, department: str, min_experience: int) -> dict:
    """
    Filters employees with more than min_experience years of experience and belonging to the specified department.
    Calculates bonuses based on their years of experience.
    """
    # Filter employees who belong to the specified department and have more than min_experience years of experience
    employees_filtered = filter(lambda employee: employee.years_of_experience > min_experience and employee.department == department, employees)
    
    # Dictionary to store employees and their bonuses
    bonus_employees = {}
    
    for employee in employees_filtered:
        bonus = employee.salary * (1 - 15/100) if employee.years_of_experience > 8 else employee.salary * 0.9
        
        bonus_employees[employee.name] = bonus
    
    return bonus_employees


def main() -> None:
    # Define the namedtuple for Employee
    Employee = namedtuple('Employee', ['name', 'department', 'salary', 'years_of_experience'])
    
    # Create a list of employees
    employees: list[Employee] = [
        Employee(name="John", department="IT", salary=1200, years_of_experience=10),
        Employee(name="Alice", department="HR", salary=500, years_of_experience=3),
        Employee(name="Bob", department="IT", salary=800, years_of_experience=7),
        Employee(name="Carol", department="Sales", salary=600, years_of_experience=4),
        Employee(name="David", department="IT", salary=1500, years_of_experience=9),
        Employee(name="Eve", department="IT", salary=1000, years_of_experience=6),
        Employee(name="Frank", department="HR", salary=450, years_of_experience=5),
        Employee(name="Grace", department="IT", salary=1100, years_of_experience=8),
        Employee(name="Hannah", department="Marketing", salary=700, years_of_experience=2),
        Employee(name="Isaac", department="IT", salary=1300, years_of_experience=12)
    ]
    
    # Department and minimum years of experience
    department: str = "IT"
    min_experience: int = 5
    
    # Get employees who qualify for bonuses and print the result
    bonus_employees = get_bonus_employees(employees, department, min_experience)
    
    if bonus_employees:
        print("Employees with bonuses:")
        for name, bonus in bonus_employees.items():
            print(f"{name}: ${bonus}")
    else:
        print("No eligible employees found.")

if __name__ == "__main__":
    main()