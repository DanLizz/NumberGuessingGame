#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random

number = random.randint(1,100)

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

def make_guess(difficulty):
  if difficulty == 'easy':
    guess = 10
  elif difficulty == 'hard':
    guess = 5
  else:
    print("Invalid input")

  while(guess != 0):
    print(f"You have {guess} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))
    if guessed_number <  number:
      print("Too low.")
      guess = guess - 1
    elif guessed_number >  number:
      print("Too high.")
      guess = guess - 1
    elif guessed_number == number:
      print(f"You got it! The answer was {number}.")
      print(art.win)
      guess = 0
    else:
      print("Invalid input")

    if guess >1:
      print("Guess again.")
    elif guess == 0:
      if guessed_number != number:
        print("You've run out of guesses, you lose.")
        print(art.lose)
make_guess(difficulty)


