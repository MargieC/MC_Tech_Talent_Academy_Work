#Task 2
import random
joke_1 = "Haha blah blah1"
joke_2 = "Haha blah blah2"
joke_3 = "Haha blah blah3"
favourite_number = int(input("Hello, what is your favourite number between 1 and a 100? "))
if favourite_number >= 0 and favourite_number <34:
    print(joke_1)
elif favourite_number >= 34 and favourite_number <67:
    print(joke_2)
elif favourite_number >= 67 and favourite_number <=100:
    print(joke_3)
else:
    print("Incorrect value selected - Number must be between 1 and 100")