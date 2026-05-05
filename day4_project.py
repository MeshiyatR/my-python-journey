#DAY 4 PROJECT - Number Guessing Game
#5th May 2026

import random

print("=" * 40)
print("     NUMBER GUESSING GAME")
print("=" * 40)
print("I an thinking of a number between 1-100")
print("=" * 40)

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

while attempts < max_attempts:
    guess = int(input(F"\nAttempt {attempts + 1}/{max_attempts} - Your guess: "))
    attempts += 1

    if guess == secret:
        print("=" * 40)
        print(f"CORRECT! You guessed it in {attempts} attempts!")
        print("=" * 40)
        break
    elif guess < secret:
        print("Too low! Try higher.")
    else:
        print("Too high! Try lower.")

    if attempts == max_attempts and guess != secret:
        print("=" * 40)
        print(f"Game over! The number was {secret}")
        print("=" * 40)
