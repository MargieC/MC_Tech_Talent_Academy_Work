#Task 2
import random
joke_1 = "Q: Why did the crab never share? A: Because he's shellfish"
joke_2 = "Q: What was the dogs favorite type of homework to do? A: A lab report"
joke_3 = "Q: What do you get if you cross an angry sheep and a moody cow? A: An animal that's in a baaaaaaaaad mooooooooooood."
favourite_number = int(input("Hello, what is your favourite number between 1 and a 100? "))
if favourite_number >= 0 and favourite_number <34:
    print(joke_1)
elif favourite_number >= 34 and favourite_number <67:
    print(joke_2)
elif favourite_number >= 67 and favourite_number <=100:
    print(joke_3)
else:
    print("Incorrect value selected - Number must be between 1 and 100")