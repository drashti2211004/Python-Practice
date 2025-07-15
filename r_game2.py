import random

# Define the choices
choices = ['stone', 'paper', 'scissors']

# Get user input
user_choice = input("Enter your choice (stone/paper/scissors): ").lower()

# Get computer's random choice using random.choice()
computer_choice = random.choice(choices)

print(f"\n You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

# Decide the winner
if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 'stone':
    if computer_choice == 'scissors':
        print("You win! Stone beats scissors.")
    else:
        print("Computer wins! Paper beats stone.")
elif user_choice == 'paper':
    if computer_choice == 'stone':
        print("You win! Paper beats stone.")
    else:
        print("Computer wins! Scissors beats paper.")
elif user_choice == 'scissors':
    if computer_choice == 'paper':
        print("You win! Scissors beats paper.")
    else:
        print("Computer wins! Stone beats scissors.")
else:
    print("Invalid choice! Please enter stone, paper, or scissors.")
