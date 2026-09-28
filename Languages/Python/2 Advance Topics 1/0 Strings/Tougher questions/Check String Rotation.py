class gpt () :
    def main() -> None:
      """
      main: Checks if one string is a rotation of another string by seeing if the rotated text is a substring of text doubled.
      
      Returns:
      None: Prints True if rotated_text is a rotation of text; otherwise, False.
      """
      text = 'waterbottle'  # input('Enter the text: ')
      rotated_text = 'erbottlewat'  # input('Enter the rotated text:')
  
      # Check if both strings have the same length and if rotated_text is a substring of text doubled
      if len(text)==len(rotated_text) and rotated_text in (text+text):
          print(True)
      else:
          print(False)
          
      return
     
    if __name__ == "__main__":
      main()


class mine () :
    def main () -> None :
      text = 'waterbottle' #input('Enter the text: ')
      rotated_text = 'erbottlewat' #input('Enter the rotated text: )
        
      for i in range( len(text) ) :
        if text == rotated_text :
          print(True)
          break
        else :
          text = text[1 : ] + text[0]
      else :
        print(False)
        
      return
    
    if __name__ == "__main__" :
      main()