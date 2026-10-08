'''
Computer to generate a number between 1-5

You have to ask the user to guess the computers number

if the user guessed it correctly
then print "You win, congrats!!"

if the user guesed it wrong
you print "Wtong guess, attempt again"

user will input again
like this they continue

they will have a total of 3 attempts

if they reach 3 attempts, then print "Attempts over, good luck next time"

'''

import random

computer_number = random.randint(1, 5)

print(computer_number)
for attemt in range(1,4):
    user_guess = int(input("guess number(between 1-5=>)"))
    if user_guess == computer_number:
        print("congrats")
        break
    else:
        print("try again")

print("attempts finish try next time")