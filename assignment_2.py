# Make a program to play rock paper scissor. The program should ask for the input for player 1 and player 2 and then
# decide and tell who wins.
import random

# Rock beats Scissor
# Paper beats Rock
# Scissor beats Paper

choices = ["rock", "paper", "scissor"]

player1choice = input("[Player 1] What do you choose: Rock, Paper or Scissor?: ").lower()
player2choice = random.choice(choices)
print(f"[Player 2] Chose: {player2choice}")

if player1choice == "rock" and player2choice == "scissor":
    print("Player1 wins")
elif player2choice == "rock" and player1choice == "scissor":
        print("Player2 wins")
elif player1choice == "paper" and player2choice == "rock":
        print("Player1 wins")
elif player2choice == "paper" and player1choice == "rock":
        print("Player2 wins")
elif player1choice == "scissor" and player2choice == "paper":
        print("Player2 wins")
elif player2choice == "scissor" and player1choice == "paper":
        print("Player2 wins")
elif player1choice == player2choice:
    print("Its a tie")