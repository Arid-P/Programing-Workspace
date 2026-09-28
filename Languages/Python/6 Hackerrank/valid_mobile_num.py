def main() -> None:
    """Main function."""
    n: int = int(input())
    
    validity: list[str | None] = []
    
    for e in range(n) :
        num: str = input()
        
        if len(num) == 10 and num[0] in {"7", "8", "9"} :
            validity.append("YES")
        else:
            validity.append("NO")
    
    for valid in validity :
        print(valid)
    
    return

if __name__ == "__main__":
    main()