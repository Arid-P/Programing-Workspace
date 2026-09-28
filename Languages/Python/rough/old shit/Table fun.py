def table(num, to):
  to += 1
  for i in range(to):
    pro = num * i
    print(num,  " * ",  i, " = ", pro)
  return 

num = int(input("Enter a number of whose table you want : "))
to = int(input("Enter a number till you want its table : "))

table(num, to)