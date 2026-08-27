"""
base information in base file
In it i have improved how is the password created by making it non-preodic and efficient
"""

import string as str
import random

#global variables
conditions: list = [] #length, lowercase, uppercase, digits, symbols, no. of password
password: str = ""


def check(current_length: int) -> bool:
    """
    Checks whether the password has reached its required length or not.
    Returns True if the length is met, False otherwise.
    """
    return current_length == conditions[0]
#end


def add_chr_1 (condition_no: int) -> str :
  """
  its takes a condition_no and then make a str choices according to the
  condition_no when called, 
  and then it take a eandom chr from choices which is added to the password
  and then returns True if password has reached its length, otherwise False
  """
  if condition_no == 1 :
    choices = str.ascii_lowercase
  elif condition_no == 2 :
    choices = str.ascii_uppercase
  elif condition_no == 3 :
    choices = str.digits
  elif condition_no == 4 :
    choices = str.punctuation
  
  return random.choice(choices)
#end 


def generate_password () -> None :
  """
  it uses the global var condition to check if that chr is suppose to be added or not
  then it generates any random number through 1 and 4 (included both) to decided which condition to add
  it adds the chr by func add_chr
  """
  global conditions, password
  password = ""
  current_length = 0
  
  while current_length < conditions[0] :
    condition_no = random.randint(1,4) # rand int for each condition
    
    if conditions[condition_no] :
      password += add_chr_1(condition_no)
      current_length += 1
    else :
      continue
      
  return
#end


def add_input_bool_to_conditions (condition) -> None :
  """
  adds the current condition to the list according to user if he wants it or not
  yes -> True
  no -> False
  """
  if (condition == "y") :
    return conditions.append(True)
  else :
    return conditions.append(False)
#end


def Inputs () -> None :
  """
  takes the inputs for conditions, and then
  add it to the conditions list by add_input_bool_to_conditions()
  it also has input validation for the int values
  it inputs the bool conditions in a loop
  """
  global conditions
  
  while True : 
    length_str: str = input("Enter the length of you password : ")
    
    try : 
      length: int = int(length_str)
      if length < 0 :
        print("Input a valid positive integer")
        continue
      
    except ValueError :
      print("Input a valid integer")
      continue
      
    else :
      conditions.append(length)
      break
  
  condition_name: list[str] = ["lowercase", "uppercase", "digits", "symbols"]
  
  for condition in condition_name :
    input_value = input(f"Do you want {condition} characters in the password (y for  yes) : ").lower()
    add_input_bool_to_conditions(input_value)
    
  while True :
    no_password_str: str = input("Enter number of passwords you want: ")
    
    try : 
      no_password: int = int(no_password_str)
      if no_password < 0 :
        print("Input a valid positive integer")
        continue
      
    except ValueError :
      print("Input a valid positive integer")
      continue
    
    else :
      conditions.append(no_password)
      break
  
  return
#end


def main() -> None :
  """
  its the main func which tells which func it suppose to come 
  """
  Inputs()
  global password, conditions
  
  for i in range(1, conditions[5]+1 ) :
    generate_password()
    print()
    print(f"password {i} : {password}")

if __name__ == "__main__" :
  main()