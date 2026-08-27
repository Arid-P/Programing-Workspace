def main () -> None :
    word1 = "abcdea"
    word2 = "bceada"
    
    for index in range(len(word1)) :
      if word1[index] not in word2 :
        return print("is not")
    
    for index in range(len(word2)) :
      if word2[index] not in word1 :
        return print("is not")
    
    return print("is")
  
if __name__ == '__main__':
  main()