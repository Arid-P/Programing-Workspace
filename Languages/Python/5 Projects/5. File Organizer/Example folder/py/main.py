"""
What to do
1. Take input for the directory: done
Possible errors: 1. Not entering a existing directory
2. change path to that directory: done
3. Genreate the list of all the files: done
4. Seperate each file_d into a list with its name and extension,so forming a nested list: done
5. Sort the list on the basis of its extension : done
6. Generate a list of all the extensions: done
7. Make folders for respective extension 
8. Move the files to their respective folders
"""
#Programing/Python/Projects/5. File Organizer/Example folder/d.java

import  os
import shutil as sh

def change_dir(path) -> None:
    os.chdir(path)
    return


def main () -> None :
    #raise ValueError('main not implemented')
    print(f"current working directory:  {os.getcwd()}\n")

    print("Enter the directory in form: 'First_folder/Second_folder/...")
    dir_str = input("Enter directory: ")

    dir_list = dir_str.split("/")
    path = os.path.join(*dir_list)

    change_dir(path)
    print(f"current working directory:  {os.getcwd()}\n")

    # change_dir("Programing/Python/Projects/5. File Organizer/Example folder/")
    
    #list of files
    content: list = os.listdir()
    #print(content)
    sep_name_content = list(map(lambda file_d: file_d.split(".") , content)) 
    files = list(filter(lambda file_d : len(file_d) == 2, sep_name_content))
    #print(files)
    
    
    #list of extensions
    extensions: list = []
    
    for file_d in files :
        if file_d[1] not in extensions:
            extensions.append(file_d[1])


    #making of folders
    for extension in extensions :
        os.mkdir(extension)


    #movinf of files :
    for ext in extensions :
        for idx, file_d in enumerate(files) :
            if file_d[1] == ext :
                sh.move((file_d[0] + '.' + file_d[1]),  ext)
            else :
                files = files[idx:]
                break

    print("All files have been Organised")
    return

if __name__ == "__main__" :
    main()