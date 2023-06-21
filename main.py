import random

class Game:

    def __init__(self):
        self.player = 0
        self.computer = 0

    def play(self):
        choice = random.randint(1, 3)
        if choice == 1:
            move = "rock"
        elif choice == 2:
            move = "paper"
        else:
            move = "scissors"

        print("The computer chose", move)

        player_move = input("Rock, paper, or scissors? ")

        if player_move == move:
            print("Tie!")
        elif player_move == "rock":
            if move == "scissors":
                print("You win!")
            else:
                print("Computer wins!")
        elif player_move == "paper":
            if move == "rock":
                print("Computer wins!")
            else:
                print("You win!")
        elif player_move == "scissors":
            if move == "paper":
                print("You win!")
            else:
                print("Computer wins!")

    def main(self):
        while True:
            self.play()
            answer = input("Play again? (y/n) ")
            if answer == "n":
                break

if __name__ == "__main__":
    game = Game()
    game.main()
