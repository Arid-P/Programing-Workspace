#details about the program in base file
#in it i add diffirent difficulties such as easy, mid, har, exterme, etc
import random 


def Try_again(diff) :
  again_check = int(input("Do want to try again (type 1 for yes) : "))
  print()
  
  if(again_check == 1) :
    diff_check = int(input("Do you want to change the difficulty (type 1 for yes) :"))
    if(diff_check == 1) :
      Select_Difficulty()
    else :
      Select_Difficulty_with_level(diff)
  else:
    print("Thanks for playing")
    return
#end


def Trys_Input (upper_bound) :
  print("Enter the number trys you will need :", end=" ")
  while 1>0 :
    tries = int(input())
    # checks if tries is in correct bound
    if(not(5 <= tries <= upper_bound )) : 
      print("Enter a valid number")
    else : 
      break
    
  return tries
#end of Trys_Input function


def Game_logic_ex () :
  tries = 5
  n = int(random.randint(1,300)) #n is our generated number
  
  trystaken = 1
  for i in range(tries) : 
    gno = int(input("Enter your guess"))
    if(n == gno) :
      print(f"You won, it took you : {trystaken} trys")
      break
    elif((n-gno) > 0) : #if the gno is smaller
      if((n - gno) > 45) :
        print("too low")
      else:
        print("little low")
    else : #if gno is greater
      if((n-gno) < (-45) ):
        print("too high")
      else:
        print("little high")
    trystaken += 1
  else :
    print(f"You lost, the number was {n} ")
    
  print()
  Try_again(4)
#end of Game_logic_easy fuction


def Game_logic_hard () :
  tries = Trys_Input(10)
  n = int(random.randint(1,200)) #n is our generated number
  
  trystaken = 1
  for i in range(tries) : 
    gno = int(input("Enter your guess"))
    if(n == gno) :
      print(f"You won, it took you : {trystaken} trys")
      break
    elif((n-gno) > 0) : #if the gno is smaller
      if((n - gno) > 35) :
        print("too low")
      else:
        print("little low")
    else : #if gno is greater
      if((n-gno) < (-35) ):
        print("too high")
      else:
        print("little high")
    trystaken += 1
  else :
    print(f"You lost, the number was {n} ")
    
  print()
  Try_again(3)
#end of Game_logic_easy fuction


def Game_logic_mid () :
  tries = Trys_Input(15)
  n = int(random.randint(1,150)) #n is our generated number
  
  trystaken = 1
  for i in range(tries) : 
    gno = int(input("Enter your guess"))
    if(n == gno) :
      print(f"You won, it took you : {trystaken} trys")
      break
    elif((n-gno) > 0) : #if the gno is smaller
      if((n - gno) > 25) :
        print("too low")
      else:
        print("little low")
    else : #if gno is greater
      if((n-gno) < (-25) ):
        print("too high")
      else:
        print("little high")
    trystaken += 1
  else :
    print(f"You lost, the number was {n} ")
    
  print()
  Try_again(2)
#end of Game_logic_mid fuction


def Game_logic_easy () :
  tries = Trys_Input(20)
  n = int(random.randint(1,100)) #n is our generated number
  
  trystaken = 1
  for i in range(tries) : 
    gno = int(input("Enter your guess"))
    if(n == gno) :
      print(f"You won, it took you : {trystaken} trys")
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
  Try_again(1)
#end of Game_logic_easy fuction


#selected difficulty but with difficulty level (1>2>3>4)
def Select_Difficulty_with_level (diff) :
  if (diff == 1) :
    Game_logic_easy()
  elif (diff == 1) :
    Game_logic_mid()
  elif (diff == 3) :
    Game_logic_hard()
  elif (diff == 4) :
    Game_logic_ex()
#end of Select_Difficulty_with_level function


def Select_Difficulty () :
  diff = input("Enter difficulty (easy, mid, hard, ex) : ")
  if (diff == "easy") :
    Game_logic_easy()
  elif (diff == "mid") :
    Game_logic_mid()
  elif (diff == "hard") :
    Game_logic_hard()
  elif (diff == "ex") :
    Game_logic_ex()
#end of Select_Difficulty function


def Start() :
  print("INSTRUCTIONS:")
  print("In this program a you need to guess a randomly generated number and minimun trys are 5")
  print()
  
  print("There are 4 difficulties: easy, medium (mid), hard, exterme (ex)")
  print()
  
  print("EASY mode rules :")
  print("In it you have to guess a munber b/w 1 to 100")
  print("If the guessed number it more or less than the selected number by more than 20 then the screen will show too high or too low respectively")
  print("If the guessed number it more or less than the selected number by 20 or less then the screen will show high or low respectively")
  print("And you get maximum of 20 trys")
  print()
  
  print("MEDIUM mode rules :")
  print("In it you have to guess a munber b/w 1 to 150")
  print("If the guessed number it more or less than the selected number by more than 25 then the screen will show too high or too low respectively")
  print("If the guessed number it more or less than the selected number by 25 or less then the screen will show high or low respectively")
  print("And you get maximum of 15 trys")
  print()
  
  print("HARD mode rules :")
  print("In it you have to guess a munber b/w 1 to 200")
  print("If the guessed number it more or less than the selected number by more than 35 then the screen will show too high or too low respectively")
  print("If the guessed number it more or less than the selected number by 35 or less then the screen will show high or low respectively")
  print("And you get maximum of 10 trys")
  print()
  
  print("EXTREME mode rules :")
  print("In it you have to guess a munber b/w 1 to 300")
  print("If the guessed number it more or less than the selected number by more than 45 then the screen will show too high or too low respectively")
  print("If the guessed number it more or less than the selected number by 45 or less then the screen will show high or low respectively")
  print("And you get 5 trys")
  print()
  
  Select_Difficulty()
#end of start function


Start()