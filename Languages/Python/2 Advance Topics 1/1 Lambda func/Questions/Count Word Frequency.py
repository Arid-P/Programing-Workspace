#for question details go to ques details.txt

from functools import reduce


def apply_conditions (ocuurences: list[tuple]) -> list[tuple] :
  
  #1. filterung the word whose occurence is more than 1
  ocuurences = filter(lambda tup : tup[1] > 1, ocuurences)
  
  #2. sorting the words alphabeticaly
  ocuurences = sorted(ocuurences, key = lambda tup: tup[0])
  
  #3. sorting the ocuurence in desencding order
  ocuurences = sorted(ocuurences, key = lambda tup: tup[1], reverse = True)
  
  return ocuurences



def main () -> None :
  #the given list
  parts_sentence: list[tuple(str)] = ["apple banana apple", "banana orange apple", "orange banana", "kiwi banana banana"]
  
  #the sum of all the elemnts in thw given list
  sentence: str = reduce(lambda part1_sentence, part2_sentence: part1_sentence + " " + part2_sentence, parts_sentence)
  
  #Unique Words in the list
  words: list[str] = list( set(sentence.split(" ") ) )
  
  ocuurences: list[tuple] = [] #store the ocuurences of a wrod in (word, ocuurence) tuple in it 
  
  for word in words :
    ocuurence = sentence.count(word)
    tup = (word, ocuurence)
    ocuurences.append(tup)
  
  ocuurences = apply_conditions(ocuurences)
  
  return print(ocuurences)


if __name__ == "__main__" :
  main()

