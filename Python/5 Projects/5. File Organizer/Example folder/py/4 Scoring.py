#details about the program in base file
#in this i add a scoring/accuray system, which save the data in a fie, as well 
import random
import datetime
import os

#change dir
os.chdir("/storage/emulated/0/Programing/Python/Projects/No. Guessing game")

#global variables
score: list[int] = []
difficulty: int = 0 #difficulty like easy, etc with its level number


def start_save_on_file () -> None :
  # Get current date and time
  now = datetime.datetime.now()
  # Format the date and time
  formatted_time = now.strftime("%d-%m-%Y %H:%M")
  
  with open("score.txt", "a") as scorefile :
    scorefile.write(f"{formatted_time} \n") #writing date and time 
  
  return

#save the score in a file named score with time and date
def save_score_on_file () -> None :
  with open("score.txt", "a") as scorefile :
    #range(len(score)-1) tells till where the last round is
    for i in range(len(score)-1) :
      scorefile.write(f"Round {i+1} : {score[i]} \n") #prints round with its accuray
  return


#end the file for next turn
def end_save_on_file () -> None :
  with open("score.txt", "a") as scorefile :
    scorefile.write(f"Overall accuray : {score[ (len(score) - 1) ]} \n")  #len(score)-1 tells the index of overallaccuray
    scorefile.write(f"\n\n")
  return
#end


#prints the score for the user
def print_score () -> None :
  totalaccuray = 0
  
  print("Your score of accuray of each round is :")
  for i in range(len(score)) :
    print(f"Round {i+1} : {score[i]}") #prints round with its accuray
    totalaccuray += score[i]
  
  overallaccuray = round( (totalaccuray/len(score)), 2)
  score.append(overallaccuray)
  
  print(f"Overall accuray : {overallaccuray}")
  print()
  return
#end


#fuction to calculate the score
def calcu_score (triestaken, tries) -> None :
  accuray = (100 - ( (triestaken / tries) * 100))
  score.append(round(accuray, 2))
  return
#end


def guessing (tries: int, n: int, guessing_range: int) -> None :
  triestaken = 0
  
  for i in range(tries) : 
    gno_str = input("Enter a number: ")
    while not gno_str.strip():
    # Check if the input is not empty
      gno_str = input('Invalid input, please enter a valid number :')
    
    gno = int(gno_str)
    
    if(n == gno) :
      print(f"You won, it took you : {triestaken + 1} tries")
      break
    
    elif((n-gno) > 0) : #if the gno is smallerq
      triestaken += 1
      if((n - gno) > guessing_range) :
        print("too low")
        continue 
      print("little low")
      
    else : #if gno is greater
      triestaken += 1
      if((n-gno) < (-guessing_range) ):
        print("too high")
        continue 
      print("little high")
    
  else :
    print(f"You lost, the number was {n} ")
    #manage till here
    
  print()
  calcu_score(triestaken, tries)
  return


def Difficulty_ex () -> None : 
  global difficulty
  difficulty = 4
  
  tries = 5
  n = int(random.randint(1,300)) #n is our generated number
  guessing_range = 45
  
  guessing(tries, n, guessing_range)
  return
#end of Difficulty_ex fuction


def Difficulty_hard () -> None :
  global difficulty
  difficulty = 3
  
  tries = Trys_Input(10)
  n = int(random.randint(1,200)) #n is our generated number
  guessing_range = 35
  
  guessing(tries, n, guessing_range)
  return
#end of Difficulty_hard fuction


def Difficulty_mid () -> None :
  global difficulty
  difficulty = 2
  
  tries = Trys_Input(15)
  n = int(random.randint(1,150)) #n is our generated number
  guessing_range = 25
  
  guessing(tries, n, guessing_range)
  return
#end of Difficulty_mid fuction


def Difficulty_easy () -> None :
  global difficulty
  difficulty = 1
  
  tries = Trys_Input(20)
  n = int(random.randint(1,100)) #n is our generated number
  guessing_range = 20
  
  guessing(tries, n, guessing_range)#
  return
#end of Difficulty_easy fuction


def change_difficulty() :
    diff_check = input("Do you want to change the difficulty (type 1 for yes) :")
    if(diff_check == "1") :
      Select_Difficulty()
    else :
      Select_Difficulty_auto()
#end

def Try_again() :
  play_again = input("Do want to try again (type 1 for yes) : ")
  print()
  
  if(play_again == "1") :
    change_difficulty()
    return
    
  print_score()
  print("Thanks for playing")
  return
#end


def Trys_Input (upper_bound)  -> int:
  print("Enter the number tries you will need :", end=" ")
  while True :
    tries_str = input()
    if tries_str.strip() :
      print("Enter a valid number")
      continue
    
    tries = int(tries_str) 
    if not(5 <= tries <= upper_bound ) :     # checks if tries is in correct bound
      print("Enter a valid number")
      continue
    break
#end of Trys_Input function


#selected difficulty but with difficulty level (1<2<3<4)
def Select_Difficulty_auto () -> None :
  global difficulty
  
  if (difficulty  == 1) :
    Difficulty_easy()
  elif (difficulty  == 2) :
    Difficulty_mid()
  elif (difficulty  == 3) :
    Difficulty_hard()
  elif (difficulty  == 4) :
    Difficulty_ex()
  
  save_score_on_file()
  Try_again()
  return
#end of Select_Difficulty_auto function


def Select_Difficulty () -> None :
  while True : 
    diff = input("Enter difficulty (easy, mid, hard, ex) : ")
    if (diff == "easy") :
      Difficulty_easy()
      break
    elif (diff == "mid") :
      Difficulty_mid()
      break
    elif (diff == "hard") :
      Difficulty_hard()
      break
    elif (diff == "ex") :
      Difficulty_ex()
      break
    else :
      print("Invalid input")
  
  save_score_on_file()
  Try_again()
  return
#end of Select_Difficulty function


def Starting_Instructions() -> None:
  print("INSTRUCTIONS:")
  print("In this program a you need to guess a randomly generated number and minimun tries are 5")
  print()
  
  print("There are 4 difficulties: easy, medium (mid), hard, exterme (ex)")
  print()
  
  print("EASY mode rules :")
  print("In it you have to guess a munber b/w 1 to 100")
  print("If the guessed number it more or less than the selected number by more than 20 then the screen will show too high or too low respectively")
  print("If the guessed number it more or less than the selected number by 20 or less then the screen will show high or low respectively")
  print("And you get maximum of 20 tries")
  print()
  
  print("MEDIUM mode rules :")
  print("In it you have to guess a munber b/w 1 to 150")
  print("If the guessed number it more or less than the selected number by more than 25 then the screen will show too high or too low respectively")
  print("If the guessed number it more or less than the selected number by 25 or less then the screen will show high or low respectively")
  print("And you get maximum of 15 tries")
  print()
  
  print("HARD mode rules :")
  print("In it you have to guess a munber b/w 1 to 200")
  print("If the guessed number it more or less than the selected number by more than 35 then the screen will show too high or too low respectively")
  print("If the guessed number it more or less than the selected number by 35 or less then the screen will show high or low respectively")
  print("And you get maximum of 10 tries")
  print()
  
  print("EXTREME mode rules :")
  print("In it you have to guess a munber b/w 1 to 300")
  print("If the guessed number it more or less than the selected number by more than 45 then the screen will show too high or too low respectively")
  print("If the guessed number it more or less than the selected number by 45 or less then the screen will show high or low respectively")
  print("And you get 5 tries")
  print()
  
  return
#end of start function


#Starting_Instructions()
start_save_on_file()
Select_Difficulty()
end_save_on_file()