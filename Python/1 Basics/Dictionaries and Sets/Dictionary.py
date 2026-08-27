# Dictionary is a data type which stores data in key : value form, key must be a unmutable data types
#  E.g. 
dict = {
  "name" : "Ari",
  "cgpa" : 4.9,
  "marks" : [99, 100, 96, 98, 92]
}
#here dict is a dictionary
print(dict)

#To access or add any value 
#dictkey"] = value

print(dict["name"])
dict["age"] = 19 #dictionaries are unmutable


#Nested Dictionary
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

#To access a value inside neseted Dictionary
print(student["subjects"]["CS"])