import random

secret_number = random.randint(1,100)
tries, guess = 0, 0
while guess != secret_number:
    guess = int(input("Take a guess: "))#Hello World
print("Hello World")
