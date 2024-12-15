import random

n = random.randint(1,100)

a = -1
Guesses = 0
while(a != n):
    a = int(input("Guess a Number: "))
    if( a > n):
        print("Choose a lower number")
    elif(a<n):
        print("Choose a higher number")
    Guesses += 1

print(f"You have guessed the correct number {n} in {Guesses} guesses")

        