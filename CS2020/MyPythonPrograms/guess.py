import random

secret_number = random.randint(1,100)
tries, guess = 0, 0
#print(secret_number)
while guess != secret_number:
    guess = int(input("I'm thinking of a number from 1 to 100, take a guess: "))
else:
    print "That's it!"
