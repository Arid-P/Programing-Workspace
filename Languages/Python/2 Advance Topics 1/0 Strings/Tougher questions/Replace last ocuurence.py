


def main () -> None :
    s: str = 'Hello World. I live in this world named earth. The earth has has a population of about 8 billion human being.'   
    ss: str = 'earth'
    ss2: str = 'world'
    ls: list[str] = s.split(ss) 
    
    new_s = ''
    for i in range(len(ls)) :
      new_s += ls[i]
      
      if i != len(ls) - 1 :
        new_s += ss
      else :
        new_s += ss2
    
    return print(new_s)

if __name__ == "__main__" :
    main()