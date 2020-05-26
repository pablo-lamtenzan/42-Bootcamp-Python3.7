import sys
import random


def parse():
    val = (input("What's your guess between 1 and 99? "))
    if val == "exit":
        return 0
    try:
        val = int(val)
    except ValueError:
        return -1
    if val > 99 or val < 1:
        return -1
    return val


print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")

to_guess = random.randint(1, 99)
if to_guess == 42:
    success_msg = "The answer to the ultimate question of life, the universe and everything is 42.\nCongratulations! You got it on your first try!"
else:
    success_msg = "Congratulations, you've got it!"

i = 1

n = parse()
while n == -1:
    print("That's not a number.")
    n = parse()
while n != to_guess:
    i += 1
    if n == 0:
        exit()
    if n < to_guess:
        print("Too low!")
    if n > to_guess:
        print("Too high!")
    if n == -1:
        print("That's not a number.")
    n = parse()
print(success_msg)
print("You won in %d attempts!" % i)
