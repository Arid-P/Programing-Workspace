import tkinter as tk

root = tk.Tk()


def print_ (arg: int | str, c)-> None :
    tk.Label(root, text=f"{arg}").grid(row = 2, column = c)


class Numbers () :

    @staticmethod
    def add_to_num (num: int) -> None :
        global num1, num2, n, r
        
        if n == 1:
            num1 = num1 * 10 + num
            
            print_(num1, 1)
            if Operations.did_switch is True :
                Operations.equal()
            
        elif n == 2:
            num2 = num2 * 10 + num
            
            print_(num2, 3)
            Operations.equal()
    
    
    @staticmethod
    def add_to_num0 () -> None :
        global num1, num2, n, r
        
        if n == 1:
            num1 = num1 * 10
            
            print_(num1, 2, 1)
            if Operations.did_switch is True :
                Operations.equal()
            
        elif n == 2:
            num2 = num2 * 10
            
            print_(num2, 3)
            Operations.equal()


class Operations () :
    operation = ""
    did_switch: bool = False
    
    @classmethod
    def set_operation (cls, op: str) -> None :
        global n 
        n = 2
        cls.operation = op
        print_(cls.operation, 2)
    
    @staticmethod
    def add () -> None :
        return Operations.set_operation("+")
    
    @staticmethod
    def subtract () -> None :
        return Operations.set_operation("-")
    
    @staticmethod
    def multiply () -> None :
        return Operations.set_operation("*")
    
    @staticmethod
    def division () -> None :
        return Operations.set_operation("/")
    
    @classmethod
    def equal (cls) -> None :
        global num1, num2
        
        if cls.operation == "+" :
            result = num1 + num2
        elif cls.operation == "-" :
            result = num1 - num2
        elif cls.operation == "*" :
            result = num1 * num2
        elif cls.operation == "t" :
            if num2 == 0:
                result = "Division by zero not possible"
            else :
                result = num1 / num2
        
        print_(f"=    {result}", 4)
    
    @classmethod
    def switch (cls) -> None :
        global n
        n = 1
        cls.did_switch = True
        return 
    
    @staticmethod
    def undo () -> None :
        global num1, num2, n, r
        
        if n == 1 :
            num1 = int(num1 / 10)
            print_(num1, 1)
        elif n == 2:
            num2 = int(num2 / 10)
            print_(num2, 3)
            Operations.equal()



def create_buttons(root):
    buttons = [
        #buttons for numbers
        [
            tk.Button(root, text="1", width=7, height=4, command=lambda: Numbers.add_to_num(1)),
            tk.Button(root, text="2", width=7, height=4, command=lambda: Numbers.add_to_num(2)),
            tk.Button(root, text="3", width=7, height=4, command=lambda: Numbers.add_to_num(3)),
            tk.Button(root, text="4", width=7, height=4, command=lambda: Numbers.add_to_num(4)),
            tk.Button(root, text="5", width=7, height=4, command=lambda: Numbers.add_to_num(5)),
            tk.Button(root, text="6", width=7, height=4, command=lambda: Numbers.add_to_num(6)),
            tk.Button(root, text="7", width=7, height=4, command=lambda: Numbers.add_to_num(7)),
            tk.Button(root, text="8", width=7, height=4, command=lambda: Numbers.add_to_num(8)),
            tk.Button(root, text="9", width=7, height=4, command=lambda: Numbers.add_to_num(9)),
            tk.Button(root, text="0", width=7, height=4, command=Numbers.add_to_num0)
        ],
        
        #buttons for operations
        [
            tk.Button(root, text="+", width=7, height=4, command=Operations.add),
            tk.Button(root, text="-", width=7, height=4, command=Operations.subtract),
            tk.Button(root, text="*", width=7, height=4, command=Operations.multiply),
            tk.Button(root, text="/", width=7, height=4, command=Operations.division),
            tk.Button(root, text="Change \nto first \nnumber", width=7, height=4, command=Operations.switch),
            tk.Button(root, text="undo", width=7, height=4, command=Operations.undo)
        ]
    ]
    return buttons


def main () -> None :
    global num1, num2, n, r
    num1, num2, n, r = 0, 0, 1, 9


    tk.Label(root, text="Result: ", width=7, height=3).grid(row=2, column=1)

    buttons = create_buttons(root)
    
    r, c, i = 5, 0, 0
    for button in buttons[0] :
        if c == 2: 
            c += 1
        button.grid(row=r, column=c)
        c += 1
        if c == 4 :
            buttons[1][i].grid(row=r, column=c)
            r, c, i = r+1, 0, i+1
    
    buttons[1][5].grid(row=r, column=1)
    buttons[1][4].grid(row=r, column=3)
    buttons[1][3].grid(row=r, column=4)
    
    r = 9
    
    tk.Label(root, text=" ", width=7, height=3).grid(row=2, column=1)

    root.mainloop()
    return

if __name__ == "__main__" :
    main()