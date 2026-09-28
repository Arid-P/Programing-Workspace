import os


def change_dir() -> None:
    os.chdir("/storage/emulated/0/Programing/Python/4 GeekforGeek/POTD/") 
    return


def change_dir_custom(month: str) -> None:
    os.chdir(f"/storage/emulated/0/Programing/Python/4 GeekforGeek/POTD/{month}/") 
    return



def main () -> None :
    months: list[str] = ["1 January", "2 February", "3 March", "4 April", "5 May", "6 June", "7 July", "8 August", "9 September", "10 October", "11 November", "12 December"]
    
    for month in months : 
        change_dir()
        # Create the folder if it does not exist
        if not os.path.exists(month):
            os.makedirs(month)
            print(f"{month=}")
            change_dir_custom(month)
            
            i, j = 0, 9
            while j < 30 :
                os.makedirs(f"{i} - {j}")
                i += 10
                j += 10
    print()


    days_in_month: list[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for idx, days in enumerate(days_in_month) :
        print(f"{days = }")
        for day in range(1, days+1) :
            if day == 1 :
                change_dir_custom(f"{months[idx]}/0 - 9")
            elif day == 10 :
                change_dir_custom(f"{months[idx]}/10 - 19")
            elif day == 20 :
                change_dir_custom(f"{months[idx]}/20 - 29")
            elif day == 30:
                change_dir_custom(months[idx])
            
            
            if not os.path.exists('example.txt') :
                file = open(f"{day}.py", "w+")
                file.close()
        


    return

if __name__ == "__main__" :
    change_dir()
    main()