"""
It is a password generator, 
it asks the user for: length, does he want: uppercase, lowerxase, digits,
symbols in the password; along with how many passwords
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
  takes the inputs for conditions and then adds it by the help of add_input_bool_to_conditions()
  """
  global conditions
  
  length = int(input("Enter the length of you password : "))
  conditions.append(length)
  
  lowercase = input("Do you want lowercase characters in the password (y for yes) : ")
  add_input_bool_to_conditions(lowercase)
    
  uppercase = input("Do you want uppercase characters in the password (y for yes) : ")
  add_input_bool_to_conditions(uppercase)
  
  digits = input("Do you want digits characters in the password (y for yes) : ")
  add_input_bool_to_conditions(digits)
    
  symbols = input("Do you want symbols characters in the password (y for yes) : ")
  add_input_bool_to_conditions(symbols)
  
  no_password = int(input("Enter number of passwords you want : "))
  conditions.append(no_password)
  
  return
#end


def main():
  
  """
  its the main func which t3lls which func it suppose to come 
  """
  Inputs()
  global password, conditions
  
  for i in range(1, conditions[5]+1 ) :
    password_creation()
    print()
    print(f"password {i} : {password}")

if __name__ == "__main__" :
  main()
