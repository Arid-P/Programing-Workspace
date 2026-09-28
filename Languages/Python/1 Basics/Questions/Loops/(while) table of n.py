#WAP to tell table of number n

n = int(input("enter a number"))

count = 1
pro = 1

while count <= 10 :
  pro = n * count
  print(f"{n} * {count} = {pro}")
  count += 1

print("END")