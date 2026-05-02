import random

print("Guess the number between 1 and 100")
cump_num = random.randint(1, 101)


for i in range(5):
    user_guess = input("Enter your Guess: (Between 1-100): ")
    try:
        user_guess = int(user_guess)
    except ValueError:
        print("Please enter a valid number between 1-100!")
        continue

    if user_guess < 1 or user_guess > 100:
        print("Please enter a number between 1-100!")
        continue
    elif user_guess == cump_num:
        print("Congratulations! You guessed the number correctly!")
        break
    elif user_guess < cump_num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

print("Game Over!")
print(f"The correct number was: {cump_num}")