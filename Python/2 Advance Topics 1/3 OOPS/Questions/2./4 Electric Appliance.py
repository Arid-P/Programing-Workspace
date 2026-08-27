class ElectricAppliance () :
    def __init__ (self, power_consumption, voltage) :
        self.power_consumption = power_consumption
        self.voltage = voltage
    
    def print_details (self) :
        print(f"Power consumption is {self.power_consumption}")
        print(f"Voltage is {self.voltage}")


class Warranty () :
    def __init__ (self, time_period) :
        self.time_period = time_period
    
    def print_details (self) :
        print(f"Time period for warranty is {self.time_period}")



class WashingMachine (ElectricAppliance, Warranty) :
    
    def __init__ (self, details: list) :
        # details = [power_consumption, voltage, time_period]
        ElectricAppliance.__init__(self, details[0], details[1])
        Warranty.__init__(self, details[2])
    
    def __str__ (self) :
        ElectricAppliance.print_details(self)
        Warranty.print_details(self)
        return "\n"


def main () -> None :
    #raise ValueError('main not implemented')
    
    lg550 = WashingMachine([2500, 100, 5])
    lg650 = WashingMachine([3000, 120, 6])
    
    print(lg550)
    print()
    print(lg650)
    
    return

if __name__ == "__main__" :
    main()