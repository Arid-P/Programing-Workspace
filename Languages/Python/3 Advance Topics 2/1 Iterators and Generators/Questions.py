from typing import Generator

class FirstnEvenNumbers:
    """prints first n even numbers"""

    def __init__(self, n) -> None:
        """Initialize FirstnEvenNumbers"""
        self.n = n
        self.current = 2
    
    def __iter__ (self) -> 'FirstnEvenNumbers' :
        return self
    
    def __next__ (self) -> int :
        if self.n >= 1 :
            value = self.current
            self.current += 2
            self.n -= 1
            return value
        else :
            raise StopIteration

class Myrange:
    """Docstring"""

    def __init__(self, start: int, stop:int, step:int) -> None:
        """Initialize Myrange"""
        self.start = start
        self.stop = stop
        self.step = step
    
    def __iter__ (self) -> 'Myrange' :
            return self
        
    def __next__ (self) -> int :
        if self.start < self.stop :
            value = self.start 
            self.start += self.step
            return value
        else :
            raise StopIteration

def square_till_n (end: int) -> Generator[int, None, None] :
    i = 1 
    while i <=end :
        yield i**2 
        i += 1

def  fibbbinaci_series () -> Generator[int, None, None] :
    a = 1 
    b = 1
    print(a)
    print(b)
    while True :
        yield a + b
        a, b = b, a + b



def main() -> None:
    """Main function."""
    n = int(input("Enter n: "))
    
    print('square_till_n')
    for i in square_till_n(n) :
        print(i)
    
    print('FirstnEvenNumbers')
    for i in FirstnEvenNumbers(n) :
        print(i)
    
    print('Myrange')
    for i in Myrange(2, 14, 3) :
        print(i)
    
    print('fibbbinaci_series')
    for i in fibbbinaci_series() :
        print(i)
        
    return

if __name__ == "__main__":
    main()