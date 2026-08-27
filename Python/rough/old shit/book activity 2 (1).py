
def print(name, e, h, m, sc, ssc):
  total = e+h+m+sc+ssc;
  average = total/5;
   
    print(print("Name of the student is ", name))
    
    print("Total = ", total, " out of 500")
    
    print("Average = ", average, "(",average,"%) out of 100(%)")
    
    return

def input():
  name = str(input("Enter the name of the student is "))
  
  moe = int(input("Enter marks of English = "))
    
  moh = int(input("Enter the marks of Hindi = "))
    
  mom = int(input("Enter the marks of Math = "))
    
  mosc = int(input("Enter the marks of Science = "))
    
  mossc = int(input("Enter the marks of Social Science = ")
    
    print(name, moe, moh, mom, mosc, mossc);
    
    return;

nofs = int(input("Enter the number of students"))
for i in range(nofs):
  print("Please enter the deatil of the ", i, " student")
  input()