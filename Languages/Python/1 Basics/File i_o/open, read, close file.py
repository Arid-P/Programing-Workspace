import os

# Change the working directory to a specific folder inside Internal Storage
os.chdir("/storage/emulated/0/Programing/Python/Basics/File i_o")  # Replace 'MyFolder' with your folder name

#print(f"path: {os.getcwd()}")  To confirm that you're in the right folder

f = open( "newfile.txt", "r")

data = f.read() #returns the data of the file in a string
print(f"whoke data : \n{data}")
f.close()

f = open( "demo1.txt", "r")

for el in range(5) :
  data = f.readline() #reads one line at a time
  print(f"{el} line : {data}")

f.close()

#in both cases once the whole data or a line is read then it cannot be read agian untill its opened again
