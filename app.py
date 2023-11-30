import random

def random_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

user_score = 0
computer_score = 0

while True:
    choice = input("Enter rock, paper, or scissors: ")
    if choice in ["rock", "paper", "scissors"]:
        computer_choice = random_choice()
        print("Your choice:", choice)
        print("Computer's choice:", computer_choice)

        if (choice == "rock" and computer_choice == "scissors") or \
           (choice == "paper" and computer_choice == "rock") or \
           (choice == "scissors" and computer_choice == "paper"):
            user_score += 1
            print("You win this round!")
        elif choice == computer_choice:
            print("It's a draw!")
        else:
            computer_score += 1
            print("Computer wins this round!")

        print("Your score:", user_score)
        print("Computer's score:", computer_score)

        continue_game = input("Do you want to continue? (Y/N): ")
        if continue_game.lower() != 'y':
            break
    else:
        print("Invalid input")

print("Final scores:")
print("Your score:", user_score)
print("Computer's score:", computer_score)