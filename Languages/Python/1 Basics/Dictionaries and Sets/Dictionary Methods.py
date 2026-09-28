student = {
  "name" : "Ari Gupta",
  "class" : 12,
  "subjects" : {
    "phy" : 97,
    "chem" : 95,
    "math" : 99,
    "CS" : 100,
    "english" : 95
  },
  "favourite subject" : "CS"
}
print(student)
print()

#Some methods or functions for dictionaries

#dict.keys() returns all the outermost keys of dict
print(f"dict.keys() : {student.keys()}")
print()

#if we want we can tyoe cast the result of .key() into a list tuole or another data type
keylist = list(student.keys())

#To find the length of the dict you xan use len(dict) or first type cast the list and then find the length of it
print(f"length of student : {len(student)} or {len(keylist)}")
print()

#dict.values is used for outputting only the values of it, you can convert into a list as well
print(f"dict.values() : {student.values()}")
print()

#dict.items() returns key and value pair as tuples, we can convert it into lists as well
print(f"dict.items() : {student.items()}")
print()

#dict.get("key") returns the value of the key, we use it as it doesnt key any error in case of wrong key
print(f"dict.get('name') :", student.get("name"))
print(f"dict.get('number') :", student.get("numberq"))
print()

#dict.update(newdict) is used to add a key value pair by either writing {"key" :value} or by declaring a new dict and using it
#If you use a key that is already decleared then the value of it will only be changed
#On trying to print it you wikl get NONE
student.update({"mobile no." : 9876784553})
print("dict.update({'key' : value }) :", student.get("mobile no."))
print()

newdict = {
  "mobile no." : 1243568790,
  "city" : "delhi"
}
student.update(newdict)
print(f"dict.update(newdict) :", student)
print()