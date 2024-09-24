#Rock-Paper-Scissors Game
#TASK 4
#User Input: Prompt the user to choose rock, paper, or scissors.
#Computer Selection: Generate a random choice (rock, paper, or scissors) for
#the computer.
#Game Logic: Determine the winner based on the user's choice and the
#computer's choice.
#Rock beats scissors, scissors beat paper, and paper beats rock.
#Display Result: Show the user's choice and the computer's choice.
#Display the result, whether the user wins, loses, or it's a tie.
#Score Tracking (Optional): Keep track of the user's and computer's scores for
#multiple rounds.
#Play Again: Ask the user if they want to play another round.
#User Interface: Design a user-friendly interface with clear instructions and
#feedback.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Main game loop."""
    user_score = 0
    computer_score = 0

    while True:
        # Get user choice
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").strip().lower()
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Get computer choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Determine winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        # Display scores
        print(f"Score - You: {user_score}, Computer: {computer_score}")

        # Ask to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
