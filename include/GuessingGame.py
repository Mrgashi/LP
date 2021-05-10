import random


def guessing_game():

    correct = random.randint(0, 100)
    loop = True
    tries = 1
    while loop:
        num = input("Guess a number between 0 and 100:")

        try:
            num = int(num)
        except:
            print("That´s not a Integer.")
            continue

        if num < correct:
            print(f"Higher...\nyou guessed {num}")
            tries += 1
        if num > correct:
            print(f"Lower...\nyou guessed {num}")
            tries += 1
        if num == correct:
            print(f"You got it.\nYou tried {tries}")
            try_again = input("Want to go another round? Y/y for 'Yes' N/n for 'No'")
            if try_again == "n" or try_again == "N":
                loop = False
            elif try_again == "y" or try_again == "Y":
                loop = True
                correct = random.randint(0, 100)
