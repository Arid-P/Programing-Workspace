def get_tries_input(upper_bound):
    while True:
        tries = int(input(f"Enter the number of tries (5 to {upper_bound}): "))
        if 5 <= tries <= upper_bound:
            return tries
        else:
            print("Invalid input. Try again.")

def try_again(diff, count):
    again_check = input("Do you want to try again? (y/n): ").lower()
    if again_check == 'y':
        diff_check = input("Do you want to change the difficulty? (y/n): ").lower()
        if diff_check == 'y':
            from game_logic import select_difficulty
            select_difficulty(count)
        else:
            from game_logic import select_difficulty_with_level
            select_difficulty_with_level(diff, count)
    else:
        from score_handler import print_score
        print_score()