class MathOperation () :
    no_operation = 0
    
    @staticmethod
    def add_number (a: int | str, b: int | str) :
        MathOperation.operation_count()
        return a + b
    
    @classmethod
    def operation_count (cls) :
        cls.no_operation += 1


def main () -> None :
    #raise ValueError('main not implemented')
    op = MathOperation
    
    print(op.add_number(10, 20))
    print(op.add_number('st', 'art'))
    print(op.no_operation)
    
    return

if __name__ == "__main__" :
    main()