from game_logic import select_difficulty
from score_handler import print_score

def starting_instructions():
    print("INSTRUCTIONS:")
    print("In this program, you need to guess a randomly generated number.")
    print("The minimum number of tries is 5.\n")

    # Difficulty Levels
    print("There are 4 difficulty levels:")
    print("1. Easy")
    print("2. Medium (Mid)")
    print("3. Hard")
    print("4. Extreme (Ex)\n")

    # Easy Mode Rules
    print("EASY Mode Rules:")
    print("- Range: 1 to 100")
    print("- Maximum number of tries: 20\n")

    # Medium Mode Rules
    print("MEDIUM Mode Rules:")
    print("- Range: 1 to 150")
    print("- Maximum number of tries: 15\n")

    # Hard Mode Rules
    print("HARD Mode Rules:")
    print("- Range: 1 to 200")
    print("- Maximum number of tries: 10\n")

    # Extreme Mode Rules
    print("EXTREME Mode Rules:")
    print("- Range: 1 to 300")
    print("- Maximum number of tries: 5\n")

    select_difficulty(1)

if __name__ == "__main__":
    starting_instructions()