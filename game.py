import random

random_number = random.randint(1, 100)
attempts = 10
i=0

while i<attempts:
  i += 1
  print(f"Attempts remaning:{attempts-i+1}")

  guess_number = int(input("Guess the number between 1 to 100:"))

  if random_number == guess_number:
    print(f"Congratulation 🥳🎉, you guess the correct number {guess_number}")
    break

  elif random_number > guess_number:
    print(f"The number is too Low! 🤔 {guess_number}")

  elif random_number < guess_number:
    print(f"The number is too High! 🤔 {guess_number}")

  else:
    print("Invalid input 😁")

  if i==attempts:
    print(f"Better luck next time 🥺, {attempts} left")
    print(f"The correct number is {random_number}")
