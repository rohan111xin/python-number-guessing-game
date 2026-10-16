import random

play_again = True

while play_again:
    random_number = random.randint(1, 100)
    attempts = 10
    i = 0
    guessed_correctly = False

    while i < attempts:
        i += 1
        print(f"Attempts remaining: {attempts - i + 1}")

        guess_number = int(input("Guess a number between 1 and 100: "))

        if random_number == guess_number:
            print(f"Congratulations! 🎉 You guessed {random_number}!")
            guessed_correctly = True
            break

        elif random_number > guess_number:
            print(f"Too low! 🤔 Your guess: {guess_number}")

        else:
            print(f"Too high! 🤔 Your guess: {guess_number}")

    if not guessed_correctly:
        print("Better luck next time! 🥺")
        print(f"The correct number was {random_number}.")

    while True:
        play = input("Play again? Press 1 for Yes or 0 for No: ")

        if play == "1":
            break

        elif play == "0":
            print("Thank you for playing! 😊")
            play_again = False
            break

        else:
            print("Invalid choice! Please enter 1 or 0.")
