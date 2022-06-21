import random

correct_guess = random.randint(0, 100)
number_count = 0
while number_count < 5:
    guessed_number = int(input("Guess a number within 0-100, both inclusive: "))
    if 0 > guessed_number < 100:
        print("Invalid entry!")
    if guessed_number > correct_guess:
        print("Too high! Try again")
    elif guessed_number < correct_guess:
        print("Too low! Try again")
    else:
        print("Awesome! You're correct.")
        break

    number_count += 1

else:
    print("Eeeyaa...! You tried but all your attempts are wrong.")
print("The correct number is", correct_guess)
