import os


def change_dir() -> None:
    os.chdir("/storage/emulated/0/Programing/Python/rough/Random questions/1")
    return


def process_file() -> int:
    no_word: int = 0
    with open('Word count.txt', 'r') as f :
        line: str = f.readline()

        while line.replace('\n', '').strip() :
            words_in_line: list = fr'{line}'.replace('\n', '').split(' ')
            no_word += len(words_in_line)
            line: str = f.readline()
            print(f'{words_in_line=}')

    return no_word


def main () -> None :
    change_dir()
    print(process_file())
    
    return

if __name__ == "__main__" :
    main()