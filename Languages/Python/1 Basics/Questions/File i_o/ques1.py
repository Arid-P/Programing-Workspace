import os

# Change the working directory to a specific folder inside Internal Storage
os.chdir("/storage/emulated/0/Programing/Python/Basic questions/file i_o")  # Replace 'MyFolder' with your folder name

#print(f"path : {os.getcwd()}") To confirm that you're in the right MyFolder


#in it wap to create a fiee with text and then replace java with python in the text
datafile = "xyz"

#writing
with open("ques1.txt", "w") as file :
  file.write("Hi everyone\nWe are learning fiee io\nusing java\nI like java")

#reading and replacing
with open("ques1.txt", "r") as file :
  datafile = file.read()
  datafile = datafile.replace("java", "python")

#writing replacement
with open("ques1.txt", "w") as file :
  file.write(datafile)

"""
programLr#rr=m
"""