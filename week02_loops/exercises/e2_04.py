"""
Number guessing game Pick a random number 1–100. Ask the user to guess,
respond higher or lower , count attempts, stop on success. Hint: while True with break ,
random.randint . Expected: Correct! You took 6 attempts.
"""
import random
def number_guessing_game():
    attempts=0
    computerguessing = random.randint(1,100)
    while True:
      attempts+=1
      userInput = int(input("Enter The Number : "))
      if userInput < computerguessing : 
          print("higher")
      elif userInput > computerguessing:
          print("lower")
      else:
          print(f"Correct! You took {attempts} attempts!")
          break
number_guessing_game()