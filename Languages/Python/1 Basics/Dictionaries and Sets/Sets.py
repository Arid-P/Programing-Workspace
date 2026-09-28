#Sets are like list mutable and each value is unique i.e. one value occurs one one time
#But the value of each ekement is immutable
#We can only store an immutable data type in it
set1 = {1,2,5,3, "hello"}
print(set1)
print()
#a set is without an index as it is sorted after declartion

#set1[0] = 3 will give an error

set2 = {1, 3, 34, 4.54, 1, 2, 764, 2} 
#As 1 nad 2 are repeated so the set will be {1,34,4.54,2,764}
print(set2)
print()

#To declare a null set 
setnul = set() #bcz setnull = {} will be a null dictionaries


#Some Methods

#set.add(el) will add  an element at last 
set1.add((1,2,4))
print(f"set1.add(el) : {set1}")
print()

#set.remove(el) removes the element from the set 
set1.remove(5)
print(f"set1.remove(el) : {set1}")
print()

#set.pop() removes a random element from the set 
set2.pop()
print(f"set2.pop(el) : {set2}")
print()

#set.union(set2) combines both sets and returns a new set
setunion = set1.union(set2)
print(f"set1.union(set2) : {setunion}")
print()

#set.intersection(set2) combines common values and returns a new set
setintersection = set1.intersection(set2)
print(f"set1.intersection(set2) : {setintersection}")
print()

#set.clear() makes the set empty or null
set1.clear()
print(f"set1.clear(el) : {set1}")
print()