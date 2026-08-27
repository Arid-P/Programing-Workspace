#question details in Ques details.txt

from functools import reduce

def main() -> None :
  words: list[str] = ["banana", "apple", "cherry", "date"]
  
  sorted_words = sorted(words, key = lambda word: word[len(word) - 1])
  
  return print(sorted_words)


if __name__ == "__main__" :
  main()