#Tuples are like lists but we cannot modify they i.e. they are mutable

tup = (1, 4, 6, 2, 2, 53, 6432, 53, 'hello')
print(tup)
print(f"Original tuple: {tup}")
#doing tup[2] = 23 wilk give an error

#we can also create null Tuples
tup2 = ()
#tup2 is a null Tuple

#for a single value tuple it is important to write a , at end otherwise it will be considered as another data type
tup3 = (34,) #tup3 is a single value tuple
a = (34) #a is condidred as a  int

#Slicing in tuple is exactly like how it is done in lists and strings 
print(f"Sliced tuple: {tup[2:6]}")


#Some functions

#tuple.index(el) tells the index of first occurence of the element el
print(f"'2' occurs first at {tup.index(2)}")

#tuple.count(el) counts the no of occurence of element el
print(f"'2' occurs {tup.count(2)} times in tup")