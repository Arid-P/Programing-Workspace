#question details in Ques details.txt

from functools import reduce

def main() -> None :
  nums: list[int] = [-3, -1, 0, 2, 4]
  
  square_nums: list[int] = list(map(lambda num: num**2, nums))
  
  sum_squared_nums: list[int] = reduce(lambda num1, num2: num1 + num2, square_nums)
  
  return print(sum_squared_nums)
  
  
if __name__ == "__main__" :
  main()