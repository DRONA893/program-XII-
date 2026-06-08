import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Enter rock, paper, or scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")

    else:
        print("Computer wins!")

    again = input("Play again? (y/n): ").lower()

    if again != "y":
        print("Thanks for playing!")
        break
