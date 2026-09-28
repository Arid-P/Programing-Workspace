def check(string: str) -> bool:
    """
    Function name: description
    
    Parameters:
    string (str): it is the string that we will check for palindrome
    
    Returns:
    bool: true if half of the elements from start and end are same otherwide False
    """
    mid_length = int(len(string)/2)
    
    for index in range(mid_length) :
      if string[index] != string[ (len(string) - 1) - index] :
        return print("it is not a palindrome")
    
    return print("it is a palindrome")



def input_variable() -> str:
    """
    it takes the input for the str variable and returns it without any
    whitespace
    """
    
    var = input("Enter the string: ")
    return var.strip()


def main () -> None :
  string = input_variable()
  check(string)
  
  return

if __name__ == "__main__" :
  main()