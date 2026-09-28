#Keywords
count = 1
sum = 0

#break, it ends the loop at its occurence 
while count <= 5 :
  sum += count 
  count += 1
  if (sum > 9) :
    break
print(f"sum is {sum} and count is {count}")

#continue makes th loop go to next itration without executing the code after it in the loop
count = 1
sum = 0

while count <= 5 :
  sum += count 
  count += 1
  if (sum > 9) :
    continue
  print(f"sum : {sum}, count : {count}")
#line; sum : 10, count : 5, and lines after it will not print as it is skiped
print(f"sum is {sum} and count is {count}")

#pass is a null statement. which does nothing it is used as a placeholder
for i in range(4)
  pass