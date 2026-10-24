def main () -> None :
  names = ['abHinav DIXit', 'AridAMAn Patel', 'ANSH singh']
  
  names_joined = ', '.join(names)
  names_joined = names_joined.lower().title()
  
  return print(names_joined)

if __name__ == "__main__" :
  main()