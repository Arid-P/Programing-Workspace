from datetime import date as d
import os

def change_dir() -> None:
    os.chdir("/storage/emulated/0/Documents/Balances") 
    return

previous_year = str(d.today().year - 1)

def main (year: str = previous_year) -> None :
    change_dir()
    lines: list[str] = []
    
    with open(f"balance {year}.txt", "r") as fi :
        lines = fi.readlines()
    
    indexs: list[int] = []
    for idx in range(5, len(lines)+3) :
        if (idx + 1) % 3 == 0 :
            indexs.append(idx)
    #print(indexs)
    print()
    
    total_max = int(lines[1].split(" = ")[1].split(" ")[0])
    total_min = int(lines[1].split(" = ")[1].split(" ")[0])
    
    for idx in indexs :
        total_curr = int( lines[idx-1].split(" = ")[1].split(" ")[0] )
        total_max = max(total_curr, total_max)
        total_min = min( total_curr, total_min)
        #print(f"{total_max = },   {idx = }")


    print(f"Maximum money in the year {year}:  {total_max}")
    print(f"Minimum money in the year {year}:  {total_min}")

    return [total_max, total_min]

if __name__ == "__main__" :
    main()