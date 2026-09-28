"""
base informatioj in base file
In it i have improved inpu and included input validation
"""

import string as str
import random

#global variables
conditions: list = [] #length, lowercase, uppercase, digits, symbols, no. of password
password: str = ""


def check (current_length: int) -> bool :
  """
  checks wheter the password has reached its required length or not
  """
  if current_length == conditions[0] :
    return True
  
  return False
#end


def password_creation () -> None :
  """
  adds chr to password one by one 
  it uses the global var condition to check if that chr is suppose to be added or not
  """
  global conditions, password
  password, random_chr = "", ""
  
  current_length= 0
  while True :
    if conditions[1] :
      random_chr = random.choice(str.ascii_lowercase)
      password += random_chr
      current_length+= 1
    
    if check(current_length) :
      break
    
    if conditions[2] :
      random_chr = random.choice(str.ascii_uppercase)
      password += random_chr
      current_length+= 1
    
    if check(current_length) :
      break
    
    if conditions[3] :
      random_chr = random.choice(str.digits)
      password += random_chr
      current_length+= 1
    
    if check(current_length) :
      break
    
    if conditions[4] :
      random_chr = random.choice(str.punctuation)
      password += random_chr
      current_length+= 1
    
    if check(current_length) :
      break
  
  return
#end


def add_input_bool_to_conditions (condition) -> None :
  """
  adds the current condition to the list according to user if he wants it or not
  yes -> True
  no -> False
  """
  if (condition == "y") :
    conditions.append(True)
  else :
    conditions.append(False)

#takes the input
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
      if length < 0 :
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


def main():
  
  """
  its the main func which tells which func it suppose to come 
  """
  Inputs()
  global password, conditions
  
  for i in range(1, conditions[5]+1 ) :
    password_creation()
    print()
    print(f"password {i} : {password}")

if __name__ == "__main__" :
  main()
