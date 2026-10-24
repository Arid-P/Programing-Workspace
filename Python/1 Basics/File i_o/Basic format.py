import os

# Change the working directory to a specific folder inside Internal Storage
os.chdir("/storage/emulated/0/Programing/Python/Basics/File i_o")  # Replace 'MyFolder' with your folder name

print(os.getcwd())  # To confirm that you're in the right folde

#there are 2 types of files
#1. text files: .txt. docs .log , etc
#2. binary files: .mp4 .mov .png .jpeg , etc

#to open a file 
#var = open("file_name", "mode") mode is w : write , r : read
f = open( "newfile.py", "r")

data = f.read() #returns the data of the file in a string
print(data)

#At end of the programm we write var.close()
f.close()