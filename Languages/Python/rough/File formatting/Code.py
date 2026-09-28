import os

os.chdir("/storage/emulated/0/Programing/Python/rough/File formatting") 

with open("Hdksjdnd.txt", "r+") as file :
  exist_in_line = "Python"
  
  while True :
    line_data = file.readline()
    print(line_data, end = "")
    
    if line_data == "\n" :
      file.write("kill")
      break
    