import random

n = random.randint(1,100)

a = -1
Guesses = 0
while(a != n):
    Guesses += 1
    a = int(input("Guess a Number: "))
    if( a > n):
        print("Choose a lower number")
    else:
        print("Choose a higher number")

print(f"You have guessed the correct number {n} in {Guesses} guesses")

        