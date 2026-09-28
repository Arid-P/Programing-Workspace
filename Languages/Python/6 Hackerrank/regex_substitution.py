import re

def main() -> None:
    no_lines: int = int(input())

    lines: list[str] = [input() for _ in range(no_lines)]

    new_lines: list[str] = []
    for line in lines:
        max_ocurr = max( line.count("&&"), line.count("||") )
        
        for i in range( max_ocurr) :
            line = re.sub(r'\s&&\s', ' and ', line)  # Replace '&&' with 'and'
            line = re.sub(r'\s\|\|\s', ' or ', line)  # Replace '||' with 'or'
        
        new_lines.append(line)

    for line in new_lines:
        print(line)

if __name__ == "__main__":
    
    main()