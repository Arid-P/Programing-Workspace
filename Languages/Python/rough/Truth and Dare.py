import random as r


def print_name (num: int) -> None :
    if num == 1:
      return 'Shrurti'
    elif num == 2:
      return 'Abhideep'
    elif num == 3:
      return 'Aridaman'
    
    return


def main() -> None :
    i: int = 1
    while i <= 3 :
      questioner: int = r. randint(1,3)
      answerer: int = r. randint(1,3)
      
      if questioner == answerer :
        continue
      else :
        print( f'Questioner: {print_name(questioner)}         Answerer: {print_name(answerer)} \n\n')
        i += 1
    
    cont: str = input('do you want to continue: ').lower().strip()
    if cont in {'', 'yes', 'y'} :
      print('\n\n')
      return main()
    
    return


if __name__ == "__main__" :
    main()
    print('storage/emulated/0/Programming/Python/rough/Random questions/1./Word count.txt')