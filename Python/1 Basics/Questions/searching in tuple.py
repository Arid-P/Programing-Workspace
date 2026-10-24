#search for a number x in following tuple

tup = (1,4,9,16,25,36,49,64,81,100)

x = int(input("enter the number : "))

idx = 0 
check = False

while idx < len(tup) :
  if (x == tup[idx]) :
    check = True
    print("Found")
  idx += 1

if(not(check)) : 
  print("Not found")