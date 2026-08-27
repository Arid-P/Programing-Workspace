import os

# Change the working directory to a specific folder inside Internal Storage
os.chdir("/storage/emulated/0/Programing/Python/Basics/File i_o")  # Replace 'MyFolder' with your folder name

# print(os.getcwd())   To confirm that you're in the right MyFolder

#use of with func
#in this ex i am opening demo4 and rwading it thrn append int it abc

with open("demo4.txt", "a+") as f :
  data = f.read()
  print(data)
  f.write("\nabc")

