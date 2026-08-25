import random

print("================================")
print("     ROCK - PAPER - SCISSORS")
print("================================")
print("Choose: rock, paper, or scissors")
print("Type 'quit' to exit the game.")

user_score = 0
computer_score = 0

while True:
    user_choice = input("\nEnter your choice: ").lower()

    if user_choice == "quit":
        break

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("Your choice:", user_choice)
    print("Computer's choice:", computer_choice)

    if user_choice == computer_choice:
        print("Result: It's a tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("Result: You win!")
        user_score += 1

    else:
        print("Result: You lose!")
        computer_score += 1

    print("Score - You:", user_score, "| Computer:", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("\n================================")
print("           FINAL SCORE")
print("================================")
print("Your score:", user_score)
print("Computer score:", computer_score)
print("Thanks for playing!")
