# File: CS112_A1_T2_3_20231133.py
# Purpose: "Perfect Square Subtraction" is a strategic game where players take turns subtracting perfect square numbers from a starting number until it reaches zero.
#Players must enter positive perfect square numbers that are less than or equal to the current number.
#The game continues until one player forces the current number to become zero. It's a battle of wits and strategy to outmaneuver the opponent and emerge victorious!
# Author: Mohamed Ahmed Sayed Hassan ElGayar
# ID: 20231133

import math


def player_move(current_number):
    while True:
        try:
            move = int(input("Enter a perfect square to subtract: "))
            if move <= 0 or math.sqrt(move) % 1 != 0:
                print("Please enter a positive perfect square number.")
            elif move > current_number:
                print("Number entered is larger than the current number. Try again.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter an integer.")


def subtract_square(current_number, move):
    return current_number - move


def main():
    current_number = int(input("Enter the starting number : "))
    player = 1

    while current_number > 0:
        print(f"Current number is : {current_number}")
        move = player_move(current_number)
        current_number = subtract_square(current_number, move) # Subtract the move from the current number
        player = 3 - player  # Switch players (1 -> 2, 2 -> 1)

    print(f"\nPlayer {3 - player} wins!")

if __name__ == "__main__":
    main()
