#for loop 
#for el in list/tuple/range() :
  #some work

list = [95, 56, 99, 97, 88, 96]

for val in list :
  print(val)
print()

#for with else is used when we use break, it executes when the whoke loop isconpleted

#for el in list
  #some work
# else:
#   some work when the loop ends


#Range function; range(el) gives a list that starts from 0 and goes to el-1, step by 1
#seq = range(5) will make seq = [0,1,2,3,4]
for i in range(6) :
  print(list[i])
print()

#way of writing range() is range(start?, stop, step?) xyz? means that its optional
for kal in range(1, 13, 2) :
  print(kal)