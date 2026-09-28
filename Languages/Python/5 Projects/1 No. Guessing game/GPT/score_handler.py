score = []

def calculate_score(trystaken, tries, count):
    percent = 100 - ((trystaken / tries) * 100)
    score.append(percent)

def print_score():
    print("Your score is:")
    for i, s in enumerate(score, 1):
        print(f"Round {i}: {s:.2f}%")
    print("Thanks for playing!")