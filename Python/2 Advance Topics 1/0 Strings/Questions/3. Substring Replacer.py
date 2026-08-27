def check_to_replace(text: str, substr: str, replace_substr: str, min_occurence: int) -> str:
    """
    check_to_replace: checks if the substring appear more thena the specified no. of time if yes then replace the substr
    
    Parameters:
    text str: the text
    substr str : the substring
    replace_substr str:the replace_substr
    min_occurence int: specified no of occurences
    
    Returns:
    str: the new or old text
    """
    
    if(min_occurence >= text.count(substr)) :
      return text.replace(substr, replace_substr)
    
    return text



def input_values() -> str:
    """
    input_values: it takes input of the text, the subtring to be replaced and the replacement substring 
    
    Returns:
    str: the text
    str : the substring
    str:the replace_substr
    """
    text: str = input("Enter the text : \n") 
    print()
    
    substr: str = input("Enter the substring tk be replaced : \n") 
    print()
    
    replace_substr: str = input("Enter the replacement substring : \n") 
    print()
    
    while True :
      min_occurence_str: str = input("Enter the minimum no of occurences of the substring : \n") 
      try: 
        min_occurence = int(min_occurence_str)
      except ValueError:
        print("enter a valid value")
      else :
        print()
        break
    
    print(check_to_replace(text, substr, replace_substr, min_occurence))
    return
  
  

if __name__ == "__main__" :
  input_values()