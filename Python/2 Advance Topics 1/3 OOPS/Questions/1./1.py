class Animal () :
    def __init__ (self, name) :
        self.name = name

    def sound (self) :
        print('Animal makes a sound')

class Dog (Animal) :
    def __init__ (self, name) :
        self.name = name

    def sound (self) :
        print(f'{self.name}: Woof')

class Cat (Animal) :
    def __init__ (self, name) :
        self.name = name

    def sound (self) :
        print(f'{self.name}: Meow')

def main () -> None :
    #raise ValueError('main not implemented')
    dog = Dog('Shera')
    cat = Cat('Milow')
    
    dog.sound()
    cat.sound()
    return

if __name__ == "__main__" :
    main()