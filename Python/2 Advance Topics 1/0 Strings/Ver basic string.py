str = "hello world, I am Aridaman Patel, I study in class 12"
print(f"Original string is: {str}\n")

#String are immutable i.e. we cannt change there value at a certain index
#e.g. str[5] = "k" will give a error

#len(str) tells the length of the string
print("Length of str:", len(str))

#Slicing
# it is taking out some part of the str
# it's done by doing str[starting index : ending index]
# we count the starting index but not the ending index

slice_str = str[7 :26] # = "I am Aridaman Patel"
print("Sliced string is:", slice_str)

#Some functions

  #str.endswith("xyz") checks wether the str ends with xyz or not  it returns True or False
print("does the string end xyz", str.endswith("class 12"))
  
  #str.capitalize() capitalizes the first ch of the str, this doesn't change the original str
change_str = str.capitalize()
print("capitalised:", str.capitalize())
  
  #str.count("xyz") counts how many times has xyz appeared in str 
print("The letter i occurs", str.count("i"), "time in string")
  
  #str.find("xyz") tells the index of the first occurence of xyz
print("i first occurs at:", str.find("i"))
print("A first occurs at:", str.find("A"))
  
  #str.replace(old, new) replaces old with new in the str, this doen't change the original string
change_str = change_str.replace("world", "")
print("world is replaced with space", str.replace("world", ""))
  
print(f"\nThe original string has become: {change_str}")
