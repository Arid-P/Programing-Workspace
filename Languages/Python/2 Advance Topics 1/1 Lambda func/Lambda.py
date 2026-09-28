from functools import reduce

def main () -> None :
  #lambda is used to create 1 liner functions
  #syntax
  #  lambda arguments or parameters : expression to be evaluated
  
  #eg, adding two number functions
  add = lambda x, y : x + y
  print(f"{add(3,5)}, {add(7,4)}")
  
  example()
  return


def example () -> None :
  #Some more examples with different functions
  
  #given a list of natural numbers create a list of squared numbers
  
  #use map fun; syntax: map(func, iterable), it is used to apply a function in all items of a iterable it doesnt geneeate a list so you have to convert it 
  
  nums = [1, 2, 3, 3, 6, 21]
  squared_nums = list(map(lambda x : x**2, nums))
  print(squared_nums)
  
  
  #fron the squared_nums lsit create a new list with only even terms from it 
  
  # use filter func; syntax: filter(function, iterable) in it the func should return a bool value it also doent generate a lisy so convert it 
  
  even_squared_nums = list(filter(lambda x: x % 2 == 0, squared_nums))
  print(even_squared_nums)
  
  
  #given a list with tuples with name and age, short it by age 
  
  #use sort, syntax: sorted(iterable, key=None, reverse=False), here key is the value or func by which it will be sorted 
  
  # List of tuples with names and ages
  people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
  
  # Sort by age (second item in each tuple)
  sorted_people = sorted(people, key=lambda person: person[1])
  sorted_people_reverse = sorted(people, key=lambda person: person[1], reverse=True)
  
  print(sorted_people)
  print(sorted_people_reverse)
  
  
  #given a lsit of number multiply all hte elements (i used the lsit nums from before)
  
  #use reduce, syntax: reduce(function, iterable), you have to import reduce from functools module 
  
  #The reduce() function from the functools module applies a specified function cumulatively to the items in an iterable, reducing it to a single result.
  
  nums = [1, 2, 3, 3, 6, 21]
  product_elements_reduce = reduce(lambda x, y: x*y, nums)
  
  product_elements_loop = 1 
  for i in range(0, len(nums)) :
    product_elements_loop *= nums[i]
    
  print(product_elements_loop)
  print(product_elements_reduce)
  
  return


if __name__ == "__main__" :
  main()
