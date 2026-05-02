import random


name_list = ["python", "siavash", "apple", "bannana", "grape", "orange"]

selected_name = random.choice(name_list).lower()

print("Welcome to game! guess the word!")

guess_count = len(selected_name)
guessed_list = ['-'] * guess_count

while guess_count > 0:
    guessed_char = input("Enter a char: \n")

    if guessed_char.isalpha():
        guessed_char = guessed_char.lower()
        if guessed_char in selected_name:
            if guessed_char in guessed_list:
                print("you have guessed before, try new character!")
            else:
                for idx, char in enumerate(selected_name):
                    if char == guessed_char:
                        guessed_list[idx] = guessed_char
                current_guess = ".join(guessed_list)"
                print(f"Good guess! => {guessed_list}")
                
                if not "-" in guessed_list:
                    print("\nCongratulations! You guessed the word correctly!")          
                    break

        else:
            print("Wrong guess! Try again.")
            guess_count -= 1
            print(f"You have {guess_count} guesses left.")
    else:
        print("Please enter a valid character!")
        continue