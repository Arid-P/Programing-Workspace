"""
What to do
1. Take input for the directory: done
Possible errors: 1. Not entering a existing directory: done

2. change path to that directory: done

3. Genreate the list of all the files: done

4. Seperate each file_d into a list with its name and extension,so forming a nested list: done
Possible problem: some fiels ddont have any extension: done

5. Sort the list on the basis of its extension : done

6. Generate a list of all the extensions: done

7. Make folders for respective extension: done

8. Move the files to their respective folders: done
"""
#Programing/Python/Projects/5. File Organizer/Example folder
#Programing/Python/Projects/5. File Organizer/Example folder 2

import  os
import shutil as sh
import datetime as dt
from pathlib import Path

def change_dir(path) -> None:
    os.chdir(path)
    file = open("log file", "w+")
    current_datetime = dt.datetime.now().strftime("%H %M %S %d %B")
    file.write(f"time of creation = {current_datetime}.\n\n")
    file.close()
    return


def check_dir_if_valid(path) -> None:
    try  :
        change_dir(path)
        return
    except FileNotFoundError :
        print("\nError: No such file or directory exits")
        print("Kindly enter a proper and valid path to the folder.")
        path_str = input("Enter path:  ")
        make_path_proper(path_str)
    
    return


def make_path_proper (path_str) -> str:
    #making the path proper
    if "/" in path_str :
        path_list = path_str.split("/")
    #elif r"\" in path_str :
#        path_list = path_str.split(r"\")
    
    if not path_list[-1].strip :
        path_list.pop(-1)
    
    path = Path(*path_list)
    return check_dir_if_valid(path)



def organize_extension () -> None :
    log_f = open("log file", "w+")
    current_datetime = dt.datetime.now().strftime("%H %M %S %d %B")
    log_f.write(f"time of writing data = {current_datetime}  \n\n")

    #list of files and folders
    contents: list = os.listdir()
    
    files = list(filter(lambda file : os.path.isfile(file), contents))
    files = list(map(lambda file_d: file_d.split(".") , files)) 
    files = list(filter(lambda file_d : len(file_d) == 2, files))
    log_f.write(f"{files = }\n")
    
    folders = list(filter(lambda folder : os.path.isdir(folder), contents))
    log_f.write(f"{folders = }\n")


    #list of extensions
    extensions: list = []
    
    for file_d in files :
        if file_d[1] not in extensions:
            extensions.append(file_d[1])
    log_f.write(f"{extensions = }\n")


    #making of folders
    for ext in extensions :
        if ext not in folders :
            os.mkdir(ext)
            log_f.write(f"created subfolders {ext}")


    #movinf of files :
    print()
    for ext in extensions :
        for idx, file_d in enumerate(files) :
            if file_d[1] == ext :
                sh.move(f"{file_d[0]}.{file_d[1]}",  ext)
                print(f"\nmoved '{file_d[0]}.{file_d[1]}'' to '{ext}' folder ")
                log_f.write(f"\nmoved '{file_d[0]}.{file_d[1]}'' to '{ext}' folder ")


    print("\nAll files have been Organised")
    log_f.write("\nAll files have been Organised\n\n")


    os.rename("log file", "log file.txt")
    log_f.close()



def main () -> None :
    print(f"current working directory:  {os.getcwd()}\n")

    #inputing path
    print("Enter the directory in form: 'First_folder/Second_folder/...")
    path_str = input("Enter directory: ")

    #making the path proper and changing to it
    make_path_proper(path_str)

    #change_dir("Programing/Python/Projects/5. File Organizer/Example folder")

    print(f"current working directory:  {os.getcwd()}\n")
    organize_extension()

    return

if __name__ == "__main__" :
    main()