#Task 1
import random
myName = input("Hello! What is your name? ")
number = random.randint(1,10)
print("Well, " +myName +" I am thinking of a number between between 1 and 10.")
guess = int(input("Take a guess "))
if guess == number:
    print("Good job, "+myName + "! You guessed my number")
else:
    print("Wrong, Better luck next time")