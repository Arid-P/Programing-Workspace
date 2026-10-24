#WAP to give the sum till n using while loop 

n = int(input("enter a number : "))
#n = 5 

count = 1
sum = 0 

while count <= n :
  sum += count
  count += 1

print(f"sum : {sum}")