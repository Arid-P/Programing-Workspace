import random
from utils import try_again, get_tries_input
from score_handler import calculate_score

def game_logic_easy(count):
    tries = get_tries_input(20)
    n = random.randint(1, 100)
    trystaken = 1

    for i in range(tries):
        gno = int(input("Enter your guess: "))
        if n == gno:
            print(f"You won, it took you {trystaken} tries!")
            break
        elif (n - gno) > 0:
            print("little low" if (n - gno) <= 20 else "too low")
        else:
            print("little high" if (gno - n) <= 20 else "too high")
        trystaken += 1
    else:
        print(f"You lost, the number was {n}")

    calculate_score(trystaken, tries, count)
    try_again(1, count)

def game_logic_mid(count):
    tries = get_tries_input(15)
    n = random.randint(1, 150)
    trystaken = 1

    for i in range(tries):
        gno = int(input("Enter your guess: "))
        if n == gno:
            print(f"You won, it took you {trystaken} tries!")
            break
        elif (n - gno) > 0:
            print("little low" if (n - gno) <= 25 else "too low")
        else:
            print("little high" if (gno - n) <= 25 else "too high")
        trystaken += 1
    else:
        print(f"You lost, the number was {n}")

    calculate_score(trystaken, tries, count)
    try_again(2, count)

def game_logic_hard(count):
    tries = get_tries_input(10)
    n = random.randint(1, 200)
    trystaken = 1

    for i in range(tries):
        gno = int(input("Enter your guess: "))
        if n == gno:
            print(f"You won, it took you {trystaken} tries!")
            break
        elif (n - gno) > 0:
            print("little low" if (n - gno) <= 35 else "too low")
        else:
            print("little high" if (gno - n) <= 35 else "too high")
        trystaken += 1
    else:
        print(f"You lost, the number was {n}")

    calculate_score(trystaken, tries, count)
    try_again(3, count)

def game_logic_ex(count):
    tries = 5
    n = random.randint(1, 300)
    trystaken = 1

    for i in range(tries):
        gno = int(input("Enter your guess: "))
        if n == gno:
            print(f"You won, it took you {trystaken} tries!")
            break
        elif (n - gno) > 0:
            print("little low" if (n - gno) <= 45 else "too low")
        else:
            print("little high" if (gno - n) <= 45 else "too high")
        trystaken += 1
    else:
        print(f"You lost, the number was {n}")

    calculate_score(trystaken, tries, count)
    try_again(4, count)

def select_difficulty_with_level(diff, count):
    if diff == 1:
        game_logic_easy(count)
    elif diff == 2:
        game_logic_mid(count)
    elif diff == 3:
        game_logic_hard(count)
    elif diff == 4:
        game_logic_ex(count)

def select_difficulty(count):
    diff = input("Enter difficulty (easy, mid, hard, ex): ").lower()
    if diff == "easy":
        game_logic_easy(count)
    elif diff == "mid":
        game_logic_mid(count)
    elif diff == "hard":
        game_logic_hard(count)
    elif diff == "ex":
        game_logic_ex(count)