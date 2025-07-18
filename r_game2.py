
        ## fixed limit 

# import random

# choices = ['stone', 'paper', 'scissors']

# user_choice = input("Enter your choice (stone/paper/scissors): ").lower()
# computer_choice = random.choice(choices)

# print("\n You chose: ', user_choice)
# print("Computer chose: ', computer_choice)

# if user_choice == computer_choice:
#     print("It's a draw!")
# elif user_choice == 'stone':
#     if computer_choice == 'scissors':
#         print("You win! Stone beats scissors.")
#     else:
#         print("Computer wins! Paper beats stone.")
# elif user_choice == 'paper':
#     if computer_choice == 'stone':
#         print("You win! Paper beats stone.")
#     else:
#         print("Computer wins! Scissors beats paper.")
# elif user_choice == 'scissors':
#     if computer_choice == 'paper':
#         print("You win! Scissors beats paper.")
#     else:
#         print("Computer wins! Stone beats scissors.")
# else:
#     print("Invalid choice! Please enter stone, paper, or scissors.")



          ## using unlimited loop 

import random

choices = ['stone', 'paper', 'scissors']

print("Welcome to Stone-Paper-Scissors!")
print("Type 'quit' anytime to exit the game.\n")


for round in range(1, 1_000_001):
    print("Round: ", round)
    
    user_choice = input("Enter your choice (stone/paper/scissors): ").lower()

    if user_choice == 'quit':
        print("Thanks for playing !!!")
        break

    # Validate input
    if user_choice not in choices:
        print("Invalid choice! Please enter stone, paper, or scissors.\n")
        continue

    computer_choice = random.choice(choices)

    print("\nYou chose: ",user_choice)
    print("Computer chose: ", computer_choice)

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

    print("\n")