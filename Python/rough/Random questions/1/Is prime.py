import math as m

def is_prime(n: int) -> bool:
    if n <= 1 :
        return False
    elif n > 2 and n % 2 == 0 :
        return False
    elif n == 2:
        return True

    for div in range(3, int(m.sqrt(n)), 2) :
        if n % div == 0 :
            return False

    return True


def main () -> None :
    n: int = int(input('Entet the num: '))
    
    text = 'is prime' if is_prime(n) else 'is not prime'
    
    print(n, text)
    return

if __name__ == "__main__" :
    main()