import random

def get_user_choice():
    user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        user_choice = input("Enter your choice: ").capitalize()
    return user_choice

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_wins = 0
    computer_wins = 0

    for _ in range(5):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_wins += 1
        elif "Computer" in result:
            computer_wins += 1

    print("\nGame Over!")
    print(f"You won {user_wins} rounds.")
    print(f"Computer won {computer_wins} rounds.")

    if user_wins > computer_wins:
        print("Congratulations! You are the overall winner.")
    elif computer_wins > user_wins:
        print("Sorry! The computer is the overall winner.")
    else:
        print("It's a tie!")

# Run the game
play_game()
