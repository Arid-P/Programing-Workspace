import os

# Change the working directory to a specific folder inside Internal Storage
os.chdir("/storage/emulated/0/Programing/Python/Basic questions/file i_o")  # Replace 'MyFolder' with your folder name

print(f"path : {os.getcwd()}")  # To confirm that you're in the right MyFolder

#In it a file (ques2.txt) is given containing a list of number separated by commas
#Find the count of even numbers

def check_number_even () :
  with open("ques 2.txt", "r") as file :
    data = file.read()
    nums: list[str] = data.split(",") #splits a string into lists by a sperater () like ',' in this case
    #in thia case the list is of a string
    
    no_type_count: int = 0
    for num in nums :
      if int(num) % 2 == 0 :
        no_type_count += 1
    
    return print(no_type_count)

check_number_even()