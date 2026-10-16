import random

play_again = True
while play_again:
    random_number = random.randint(1, 100)
    attempts = 10
    i = 0
    guessed_correctly = False

    print("\n🎮 Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")

  
    while i < attempts:
        print(f"\nAttempts remaining: {attempts - i}")

        try:
            guess_number = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue

        if guess_number < 1 or guess_number > 100:
            print("Please enter a number between 1 and 100.")
            continue

        i += 1

        if random_number == guess_number:
            print(f"Congratulations! 🎉 You guessed {random_number}!")
            guessed_correctly = True
            break

        elif guess_number < random_number:
            print(f"Too low! 🤔 Your guess: {guess_number}")

        else:
            print(f"Too high! 🤔 Your guess: {guess_number}")

    if not guessed_correctly:
        print("\nBetter luck next time! 🥺")
        print(f"The correct number was {random_number}.")

    while True:
        play = input(
            "\nPlay again? Press 1 for Yes or 0 for No: "
        ).strip()

        if play == "1":
            break

        elif play == "0":
            print("Thank you for playing! 😊")
            play_again = False
            break

        else:
            print("Invalid choice! Please enter 1 or 0.")

print("Game closed. See you next time! 👋")
