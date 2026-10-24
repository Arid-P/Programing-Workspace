#given a lsit with names of fruits, sort it by the length of their names 

def sort_len_name (fruits: list[str]) -> list[str] :
  sorted_fruits = sorted(fruits, key = lambda fruit: len(fruit))
  
  return sorted_fruits

if __name__ == "__main__" :
  fruits = ['kiwi', 'banana', 'apple', 'watermelon', 'mango', 'sitaphal', 'dragon fruit']
  print(sort_len_name(fruits))