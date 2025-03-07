import random
import math
7git ad
target = random.randint(1, 9)
while True:
    guess = int(input("enter your guess between 1 and 9"))
    if guess == target:
        print("congratulation you guessed right number")
        break
    elif guess > target:
        print("your guess is too high")
    else:
        print("too low")
