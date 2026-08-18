import random

random_number = random.randint(0, 20)
guess_number = input("Guess a number between 1 and 20: ")
guess_number = int(guess_number)

while random_number != guess_number:
    if random_number > guess_number:
        print ("Your guess is less than the random number")
    else:
        print ("Your guess is greater than the random number")
    guess_number = input("Guess a number between 1 and 20: ")
    guess_number = int(guess_number)

print ("You guessed the number")
