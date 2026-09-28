import time as t

def greeter(name:str):
    def greeting (message: str) -> str :
        return f'{message}, {name}'
    return greeting

def check_non_negative (func) :
    def wrapper (*args, **kwargs) :
        print(f'Calling {func} with {args} and {kwargs} argument')
        
        for el in args :
            if el < 0 :
                print('Warning: one of the arguments passed into multiply is negative')
        
        for el in kwargs.values() :
            if el < 0 :
                print('Warning: one of the arguments passed into multiply is negative')
        
        return func(*args, **kwargs)
    
    return wrapper

def time_it (func) :
    def wrapper (*args, **kwargs) :
        print(f"Running {func.__name__}")
        start_time = t.time()
        print(f'Result = {func(*args, **kwargs)}')
        end_time = t.time()
        
        time_taken = end_time - start_time
        print(f"Time taken: {time_taken:.5f} seconds")
    return wrapper

calls = 0
def limit_calls (func) :
    def wrapper (*args, **kwargs) :
        global calls
        calls += 1
        if calls <= 3 :
            func(*args, **kwargs)
        else :
            print("Call limit reached")
        
    return wrapper
    


@check_non_negative
def multiply (x: int, y: int) -> int :
    return print(x * y)

@limit_calls
def greet():
    print("Hello!")

@time_it
def main() -> None:
    """Main function."""
#greeter{
    greet_ari = greeter("Ari")
    greet_world = greeter("World")
    print(greet_ari('Hello'))
    print(greet_world('Hello'))
#}

#check_non_negative{
    multiply(2, 4)
    multiply(-3, 5) 
#}

#limit_calls{
    greet()
    greet()
    greet()
    greet()
    greet()
#}

    return 'successful run'

if __name__ == "__main__":
    main()