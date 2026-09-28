#details about the program in base file
#in it trying again funcrion is added
import random 

#give you the option of trying again
def Try_again() :
  check = int(input("Do want to try again (type 1 for yes) : "))
  print()
  
  if(check == 1) :
    Game_logic()
  else:
    print("Thanks for playing")


#all of the main game logic
def Game_logic() :
  trys = int(input("Enter the number trys you will need (b/w 3 to 20) : "))
  
  n = int(random.randint(1,100)) #n is our generated number
  
  trystaken = 1
  for i in range(trys) : 
    gno = int(input("Enter your guess"))
    
    if(n == gno) :
      print(f"You won, it took you : {trystaken}")
      break
    
    elif((n-gno) > 0) : #if the gno is smaller
      if((n - gno) > 20) :
        print("too low")
      else:
        print("little low")
        
    else : #if gno is greater
      if((n-gno) < (-20) ):
        print("too high")
      else:
        print("little high")
    
    trystaken += 1
    
  else :
    print(f"You lost, the number was {n} ")
  print()
  Try_again()



#starts the game by telling all the instructions
def start() :
  print("INSTRUCTIONS:")
  print("In this game a you need to guess a randomly generated number b/w 1 and 100.")
  print("If the guessed number it more or less than the selected number by more than 20 then the screen will show too high or too low respectively")
  print("If the guessed number it more or less than the selected number by 20 or less then the screen will show high or low respectively")
  print()
  Game_logic()



start() #games starts