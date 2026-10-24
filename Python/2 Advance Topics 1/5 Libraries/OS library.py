# Notes for `os` Library
# This file contains explanations and code examples for working with the `os` library in Python.

# 1. Importing the `os` Library
# To use the `os` library, you need to import it first.
import os

# 2. Working with File and Directory Paths
# a. Getting the current working directory
# - os.getcwd(): Returns the current working directory as a string.
print(f"Current Working Directory: {os.getcwd()}")

# b. Changing the current working directory
# - os.chdir(path): Changes the current working directory to the specified path.
# - This can be useful for organizing or changing context when working with files.
# Example: Uncomment the following lines if you have a valid directory to test with.
# os.chdir('/path/to/your/directory')  # Change to the specified directory
# print(f"Changed to new directory: {os.getcwd()}")

# c. Joining paths
# - os.path.join(path, *paths): Joins one or more path components intelligently.
# It is useful for creating platform-independent paths.
# Example of Joining Paths
folder = "Documents"
subfolder = "Projects"
filename = "project_file.txt"

# Combine these components into a complete path
path = os.path.join(folder, subfolder, filename)

# Print the resulting path
print(f"Joined Path: {path}")
# Output will vary based on the platform:
# On Linux/macOS: Documents/Projects/project_file.txt
# On Windows: Documents\Projects\project_file.txt

# 3. Working with Directories
# a. Listing files and directories
# - os.listdir(path): Returns a list of the entries in the directory given by `path`.
print(f"Files and directories in the current directory: {os.listdir('.')}")

# b. Creating a directory
# - os.mkdir(path): Creates a directory at the specified `path`. 
# - os.makedirs(path): Creates directories recursively, including any intermediate directories.
os.mkdir("new_directory")  # Create a single directory
os.makedirs("parent_directory/child_directory")  # Create nested directories

# c. Removing a directory
# - os.rmdir(path): Removes a directory at the specified `path` (only if it's empty).
# - os.removedirs(path): Removes directories recursively.
os.rmdir("new_directory")  # Remove an empty directory
os.removedirs("parent_directory/child_directory")  # Remove nested directories

# 4. Working with Files
# a. Creating and opening a file
# - open(path, mode): Opens a file in the specified mode. The mode could be 'r', 'w', 'a', etc.
file = open("example.txt", "w")  # Open a file in write mode
file.write("This is an example file!")  # Write content to the file
file.close()  # Close the file to save changes

# b. Reading from a file
# - open(path, mode): Open the file and use methods like read(), readline(), or readlines().
file = open("example.txt", "r")  # Open a file in read mode
content = file.read()  # Read the entire content of the file
print(f"Content of 'example.txt':\n{content}")
file.close()

# c. Removing a file
# - os.remove(path): Removes the file at the specified `path`.
os.remove("example.txt")  # Delete the file

# 5. Checking File and Directory Status
# a. Checking if a file or directory exists
# - os.path.exists(path): Returns True if the file or directory exists, False otherwise.
print(f"Does 'example.txt' exist? {os.path.exists('example.txt')}")
print(f"Does 'new_directory' exist? {os.path.exists('new_directory')}")

# b. Checking if it's a file or directory
# - os.path.isfile(path): Returns True if the path points to a file.
# - os.path.isdir(path): Returns True if the path points to a directory.
print(f"Is 'example.txt' a file? {os.path.isfile('example.txt')}")
print(f"Is 'new_directory' a directory? {os.path.isdir('new_directory')}")

# 6. Environment Variables
# a. Getting the value of an environment variable
# - os.environ: A dictionary-like object representing the environment variables.
# Example of Accessing Environment Variables
path_variable = os.environ.get("PATH")
print(f"System PATH variable: {path_variable}")

# b. Setting a custom environment variable
# - os.environ[key] = value: Sets an environment variable in the current session.
os.environ["MY_VAR"] = "Hello, Environment Variables!"

# Accessing the custom environment variable
my_var_value = os.environ.get("MY_VAR")
print(f"Custom Environment Variable MY_VAR: {my_var_value}")
# Note: Environment variables set using os.environ only last during the current session.

# 7. Running System Commands
# a. Running a system command using os.system()
# - os.system(command): Runs the system command (returns the exit status).
# WARNING: This method is not recommended for handling user input due to potential security risks.
exit_status = os.system("echo 'Hello from the system!'")
print(f"Exit status of system command: {exit_status}")

# 8. Other Useful Functions
# a. Getting the current user's name
# - os.getlogin(): Returns the name of the user currently logged in.
print(f"Current user: {os.getlogin()}")

# b. Getting the current process ID
# - os.getpid(): Returns the current process ID.
print(f"Current process ID: {os.getpid()}")