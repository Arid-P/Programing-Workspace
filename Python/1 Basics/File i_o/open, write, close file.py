import os
# Change the working directory to a specific folder inside Internal Storage
os.chdir("/storage/emulated/0/Programing/Python/Basics/File i_o")  # Replace 'MyFolder' with your folder name
#print(f"path: {os.getcwd()}")  To confirm that you're in the right folder

#writing can be done by either 'a' -> adds data at the end or w' -> overwrites the whoke data 
#if the dike doesnt exists then it creates one
f = open( "demo2.txt", "a")

f.write("\nHello world, append case")
f.close()

f = open( "demo3.txt", "w")

f.write("Hello] world, writing case")
f.close()

