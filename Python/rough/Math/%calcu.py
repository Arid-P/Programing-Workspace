#dont change anything from here onwards otherwise it might not work
from icecream import ic

def printing_percentage (subjects, percentage) :
    sum: float = 0.0
    for i in range(0, len(subjects)) :
      ic(subjects, percentage)
      sum += percentage[i]
    
    print()
    print(f"Total : {round( (sum/6), 2)}%")
    
    return
#end

def periodic_percent_calcu (marks: list[float]) : 
    percent: float = 0
    
    for i in range(0, len(subjects)) :
      percent = marks[i] * (100/20)
      percentage.append(round(percent, 2))
    return
#end 


def annual_percent_calcu (marks: list[float]) :  
    percent: float
    
    for i in range(0, (len(subjects)-1)) : 
    #calculating the percentage till math leaving computer
      percent = float(marks[i]) * (100/80)
      percentage.append(round(percent, 2))
    
    percentage.append(marks[5] * 2)

    return
#end 


def inp_exam () :  
  print("Type ")
  print("  pt for periodic test which is of 20 marks, or ")
  print("  hy or ann for half yearly or annual exam which is of 80 marks")
  
  while True :
    examstr = input("Please enter the exam : ").lower()
    
    if examstr in ['pt', 'hy', 'ann'] :
      return examstr
    else :
      print("enter a vaild input (i.e. , pt, hy or ann")
      continue
#end


def select_exam (examstr: str) :  
    if examstr == "pt" :
      print()
      periodic_percent_calcu(marks)
      
    elif examstr == "hy" or examstr == "ann" :
      print()
      annual_percent_calcu(marks)
    
    return
#end

examstr = inp_exam()

subjects: list[str] = ["english", "sc", "ssc", "hindi", "math", "computer"]

percentage: list[float] = []

n = len(subjects)
n = 0
marks = [63, 77, 64, 51, 74, 4]
for i in range(0, n) :
  marks.append(input(f"Kindly enter your {subjects[i]} marks : "))
  
  
select_exam(examstr)
printing_percentage(subjects, percentage)