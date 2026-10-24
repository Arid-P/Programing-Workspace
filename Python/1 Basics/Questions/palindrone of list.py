#WAP to check if a list is palindrone or not
#E.g.   list = [1, 'abc', 'hi', 'abc', 1] is a palindrone list

list = [1, 2, 3, 'hi', 6, 3, 2, 1]

#for inputing you can use list.append(input())

copylist = list.copy()
copylist.reverse()
#you cannot do list.reverse as it give NONE as its output so copylist will equal NONE
print(f"{list=},    \n{copylist=}")

if (list == copylist) :
  print(f"The list: {list}; Is a palindromic list")
else:
  print(f"The list: {list}; Is not a palindromic list")