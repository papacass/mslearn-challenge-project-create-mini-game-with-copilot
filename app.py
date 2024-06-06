# rock paper scissors game
import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It\'s a draw!'
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return 'You win!'
    else:
        return 'You lose!'

def play_game():
    user_score = 0
    computer_score = 0
    draws = 0
    rounds = 0
    is_champion = False

    while True:
        valid_choices = ['rock', 'paper', 'scissors']
        user_choice = input('Enter your choice (rock, paper, scissors): ').lower()

        if user_choice == 'champion':
            print('You are too good at this game! The computer doesn\'t want to play with you.')
            is_champion = True
            break

        while user_choice not in valid_choices:
            print('Invalid choice. Please enter rock, paper, or scissors.')
            user_choice = input('Enter your choice (rock, paper, scissors): ').lower()
        computer_choice = get_computer_choice()
        print('Computer chose:', computer_choice)
        result = determine_winner(user_choice, computer_choice)
        print(result)

        rounds += 1

        if result == 'You win!':
            user_score += 1
        elif result == 'You lose!':
            computer_score += 1
        else:
            draws += 1

        print(f'Scores: Player - {user_score}, Computer - {computer_score}, Draws - {draws}')

        play_again = input('Do you want to play again? (y/n): ').lower()
        if play_again != 'y':
            break

    if not is_champion:
        print(f'Final scores after {rounds} rounds: Player - {user_score}, Computer - {computer_score}, Draws - {draws}')
        if user_score > computer_score:
            print('Overall winner: Player')
        elif computer_score > user_score:
            print('Overall winner: Computer')
        else:
            print('The game is a draw')

play_game()