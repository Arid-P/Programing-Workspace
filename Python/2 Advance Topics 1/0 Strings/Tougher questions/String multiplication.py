def make_equal(max_num:str, min_num:str) -> str:
    for i in range(int(max_num) - int(min_num)) :
      min_num = ("1" + min_num) 
    
    return min_num


def string_multiply (max_num: str, min_num: str) -> int :
    carry: int = 0
    product: list[str] = []
    
    for i in range(-1, -len(min_num)-1, -1) :
      pro = str( + carry)
      print(pro)
      if len(pro) > 1 :
        carry = pro[0]
      else :
        carry = 0
      
      product.append(pro[-1])
    
    if carry != 0 :
      product.append(str(carry))
    
    print(product)
    product.reverse()
    print(product)
    
    return int(''.join(product))


def input_valided() -> str:
    num = input('Enter the number')
    try :
      num = int(num)
    except ValueError :
      print("Enter a valid value")
      return input_valided()
    else :
      return str(num)


def main() -> None:
    num1: str = "12" #input_valided()
    num2: str = "4" #input_valided()
    
    print(string_multiply(num1, num2))
    return

if __name__ == "__main__" :
    main()