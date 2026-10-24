"""
Program 17: Random Module — Dice Rolling Simulator & Guessing Game
CBSE Class 11 Practical File

Objective:
1. Use the `random` module (`random.randint`) to simulate rolling a pair of 6-sided dice N times.
   Generate a frequency distribution of the resulting sums (2 through 12).
2. Implement a number guessing game where the computer picks a random secret number
   between 1 and 100, and the user guesses with feedback ('Too high', 'Too low', 'Correct!')
   within a maximum allowed attempt limit.
"""

from random import random, randint


def simulate_dice_rolls(num_rolls: int) -> dict[int, int]:
    """
    Simulate rolling two 6-sided dice `num_rolls` times.
    Each die produces a value from 1 to 6 (inclusive) using random.randint.

    Parameters:
        num_rolls (int): Total number of simulation rolls (must be > 0).

    Returns:
        dict[int, int]: Frequency map of sums from 2 to 12.
                        Keys are integers 2..12, values are counts.

    Raises:
        ValueError: If num_rolls <= 0.
    """
    if num_rolls <= 0:
        raise ValueError("num rolls cannot be 0")

    freq: dict[int, int] = {i: 0 for i in range(2, 13)}
    while num_rolls > 0:
        die1: int = randint(1, 6)
        die2: int = randint(1, 6)

        total: int = die1 + die2
        freq[total] += 1
        num_rolls -= 1

    return freq


def play_guessing_game(secret_number: int, guess: int) -> str:
    """
    Evaluate a player's guess against the secret number.

    Parameters:
        secret_number (int): The target number.
        guess (int): The player's guess.

    Returns:
        str: "Too low", "Too high", or "Correct!"
    """
    if guess < secret_number:
        return "Too low"
    elif guess > secret_number:
        return "Too high"
    else:
        return "Correct!"


if __name__ == "__main__":
    print("--- Program 17: Random Module Applications ---")
    print("1. Dice Rolling Simulator")
    print("2. Number Guessing Game")
    choice = input("Select an option (1 or 2): ").strip()

    if choice == "1":
        rolls = int(input("\nEnter number of dice rolls to simulate: "))
        if rolls <= 0:
            print("Number of rolls must be positive.")
        else:
            freq_map = simulate_dice_rolls(rolls)
            print(f"\n--- Simulation Results ({rolls} rolls) ---")
            print(f"{'Sum':<6} {'Count':<10} {'Percentage':<10}")
            print("-" * 28)
            for s in range(2, 13):
                count = freq_map.get(s, 0)
                pct = (count / rolls) * 100
                print(f"{s:<6} {count:<10} {pct:.2f}%")

    elif choice == "2":
        secret = randint(1, 100)
        max_attempts = 7
        print(f"\nI have picked a secret number between 1 and 100.")
        print(f"You have {max_attempts} attempts to guess it.")

        won = False
        for attempt in range(1, max_attempts + 1):
            user_guess = int(
                input(f"\nAttempt {attempt}/{max_attempts} - Enter guess: ")
            )
            feedback = play_guessing_game(secret, user_guess)
            print(f"Feedback: {feedback}")

            if feedback == "Correct!":
                print(f"Congratulations! You guessed the number in {attempt} attempts!")
                won = True
                break

        if not won:
            print(f"\nGame Over! The secret number was {secret}.")
    else:
        print("Invalid choice.")
