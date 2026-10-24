from abc import ABC, abstractmethod


class Employee (ABC) :
    @abstractmethod
    def calculate_salary() -> None :
        pass


class FullTimeEmpolyee (Employee) :
    status = "Full Time"
    __salary_per_hr = 100
    
    def __init__ (self, name) :
        self.name = name
    
    def calculate_salary (self, hrs_worked) :
        self.__salary = hrs_worked * self.__salary_per_hr
    
    def get_salary (self) :
        print(f"One month salary of {self.name}'s  = {self.__salary}")
    
    @classmethod
    def set_per_hr_rate (cls, rate) :
        cls.__salary_per_hr = rate
    


class PartTimeEmpolyee (Employee) :
    status = "Part Time"
    __salary_per_hr = 70
    
    def __init__ (self, name) :
        self.name = name
    
    def calculate_salary (self, hrs_worked) :
        self.__salary = hrs_worked * self.__salary_per_hr
    
    def get_salary (self) :
        print(f"One month salary of {self.name}'s  = {self.__salary}")
    
    @classmethod
    def set_per_hr_rate (cls, rate) :
        cls.__salary_per_hr = rate
    


def main () -> None :
    #raise ValueError('main not implemented')
    rohan = FullTimeEmpolyee('Rohan')
    jayesh = PartTimeEmpolyee('Jayesh')

    rohan.calculate_salary(150)
    jayesh.calculate_salary(170) 

    rohan.get_salary()
    jayesh.get_salary()
    
    FullTimeEmpolyee.set_per_hr_rate(115)
    PartTimeEmpolyee.set_per_hr_rate(85)

    return

if __name__ == "__main__" :
    main()
