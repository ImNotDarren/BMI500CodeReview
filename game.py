import random

# This is a ‘Rock, Paper, Scissors’ game
choices = ['rock', 'paper', 'scissors']


# Player class to represent the player's name and score
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    # Player randomly chooses either "rock", "paper", or "scissors"
    def play(self):
        return random.choice(choices)

    def add_score(self):
        self.score += 1

    def __str__(self):
        return f"{self.name} has {self.score} points."


# Function to determine the winner of a round
def determine_winner(player1, player2):
    if player1 == player2:
        return -1
    elif (player1 == "rock" and player2 == "scissors") or \
            (player1 == "scissors" and player2 == "paper") or \
            (player1 == "paper" and player2 == "rock"):
        return 1
    else:
        return 0


# Function to play the game
def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    player1 = Player('Player 1')
    player2 = Player('Player 2')

    while True:
        # Get player's choice
        player_choice = player1.play()
        print(f"{player1.name} chooses {player_choice}")

        # Randomly choose for the computer
        computer_choice = player2.play()
        print(f"{player2.name} chooses {computer_choice}")

        # Determine the winner
        result = determine_winner(player_choice, computer_choice)
        if result == 1:
            player1.add_score()
            print(f"{player1.name} gets one score!")

        elif result == 0:
            player2.add_score()
            print(f"{player2.name} gets one score!")

        else:
            print("It's a tie!")

        print('-' * 30)

        # Check if Player 1 has reached 2 points and won the game
        if player1.score == 2:
            print(f"{player1.name} wins!")
            break

        # Check if the Computer has reached 2 points and won the game
        if player2.score == 2:
            print(f"{player2.name} wins!")
            break


if __name__ == '__main__':
    play_game()
