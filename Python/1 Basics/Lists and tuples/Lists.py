# Lists are like array but they can store different data types 
markslist = ["Arjun", 95, "Rahual", 89.9]
print(f"Original list: {markslist}")

# lists are mutable i.e. we can modify their value at a certain index
markslist[3] = 92.4


#Slicing
#it exactly like how you do it in a string 
print(f"Sliced list: {markslist[1:3]}")


#Some functions, these all function directly change the list

numlist = [ 1, 3, 7, 3, 43, 23, 245]
fruitlist = ["litches", "appkes", "guava", "banana"]

#list.append("el") it adds an element at the end of the List 
numlist.append(98) 
# adds 98 at the end of list
print(f"appended list: {numlist}")

#list.insert(idx, el) it change the value of the element at index idx to el in the list
numlist.insert(-1, 75)
#inserts 75 inplace of 7 at index 3
print(f"instered 75 at index -1, new list: {numlist}")

#list.remove(el) it remove the first occuren of el in the list, making the list shorter
numlist.remove(3) 
# remove the first occurence i.e. index 1
print(f"removed 3 at idx 1: {numlist}")

#list.pop(idx) remove the element at index idx 
numlist.pop(2) 
# removes 3 at index 2
print(f"poped elemnt at index 2: {numlist}")

#list.reverse() it simply reverse the list i.e. val at idx 0 at last and so on
numlist.reverse()
print(f"reversed list: {numlist}")

#list.sort() is sorts the list in ascending order, works if only one data type
numlist.sort()
print(f"numlist sorted in ascending order: {numlist}")

fruitlist.sort() 
#sorts the list alphabetically
print(f"fruitlist sorted in ascending order: {fruitlist}")

#markslist.sort() will give an error as it includes differnet data types

#list.sort(reverse=True) is sorts the list in descending order, works if only one data type
numlist.sort(reverse=True)
print(f"numlist sorted in descending order: {numlist}")

fruitlist.sort(reverse=True) 
#sorts the list alphabetically
print(f"fruitlist sorted in descending order: {fruitlist}")