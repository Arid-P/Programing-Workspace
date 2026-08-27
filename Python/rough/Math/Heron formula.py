import math as m


def input_() -> None:
    #fdoc
    num = input('enter the side lenth: ')
    
    try :
      num = int(num)
    except ValueError :
      print('enter a valid value')
      return input_()
    else :
      return input_
    
    return


def main () -> None :
    a = input_()
    b = input_()
    c = input_()
    
    s = (a + b + c) / 2
    
    area = s * (s - a) * (s - b) * (s - c) 
    
    print(f" area without root = {area}")
    print(f" area with root = {m.sqrt(area)}")
    return

if __name__ == "__main__" :
    main()