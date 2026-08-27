from collections import Counter as cou

def main () -> None :
    vowel: list = ['a', 'e', 'i', 'o', 'u']
    text: str = input('Enter text: ')

    alpha_count = cou(text.strip())
    
    #print(f"{alpha_count=}")
    vowel_ocurence = 0
    for chr_ in vowel :
        #print(f"{alpha_count[chr_]},  {chr_=}")
        vowel_ocurence += alpha_count[chr_]
    
    print(f"{vowel_ocurence=}")
    return

if __name__ == "__main__" :
    main()