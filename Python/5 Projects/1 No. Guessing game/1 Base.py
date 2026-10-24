"""
In it program will genrate a nukber b/w 1 and 100 and the user has guess that no with the help of hints
if the guessed no. gno is more or less the our number n by 20 then say low and high accordingly
if more or less by more than 20 then too high and low accordingly
The number of trys will be fixed by the user
"""

import random 

print("INSTRUCTIONS:")
print("In this game a you need to guess a randomly generated number b/w 1 and 100.")
print("If the guessed number it more or less than the selected number by more than 20 then the screen will show too high or too low respectively")
print("If the guessed number it more or less than the selected number by 20 or less then the screen will show high or low respectively")
print()

trys = int(input("Enter the number trys you will need (b/w 3 to 20) : "))

n = int(random.randint(1,100)) #n is our generated number

trystaken = 1
for i in range(trys) : 
  gno = int(input("Enter your guess"))
  
  if(n == gno) :
    print(f"You won, it took you : {trystaken}")
    break
  
  elif((n-gno) < 0) : #if the gno is greater
    if((n - gno) <= (-20)) :
      print("little high")
    else:
      print("too high")
      
  else : #if gno is smaller
    if((n-gno) <= (20) ):
      print("little low")
    else:
      print("too low")
  trystaken += 1
  
else :
  print(f"You lost, the number was {n} ")