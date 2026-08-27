#for question details go to ques details.txt

def sort_by_len_name (words: list[str]) -> list[str] :
  return sorted(words, key = lambda word: len(word))


def main () -> None :
  words = ["Apple", "banana", "Cherry", "apple", "Date", "cherry"]
  
  rm_duplicate_words = list( set( map( lambda word : word.lower(), words ) ) )
  
  return print(sort_by_len_name(rm_duplicate_words))


if __name__ == "__main__" :
  main()

