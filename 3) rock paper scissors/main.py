import random

# write a limit that the player can choose how many games he can play
# make choosing the option NOT CASE SENSETIVE

# idea for later project = make rock paper scissors with sockets, to have 2 players againts each other.


class RockPaperScissors:
    def __init__(self, computer_opponent):
        self._choice_interpreter = {0: "Rock", 1: "Paper", 2: "Scissors"}
        self._player1choice = None
        self._player2choice = None #computer will be defaulted as player 2

        if computer_opponent.lower().strip() == "true":
            self._computer_opponent = True
        else:
            self._computer_opponent = False

        self._player_turn = 1

    def switch_turn(self):
        if self._player_turn == 1:
            self._player_turn = 2
        else:
            self._player_turn = 1

    def generate_computer(self):
        self._player2choice = random.randint(0, 2)
        self.switch_turn()
        return self._player2choice

    def generate_player(self):
        while True:
            try:
                choice = int(input(f"your turn, player {self._player_turn}. Choose: \n 0 for rock\n 1 for paper\n 2 for scissors\n"))
                if self._player_turn == 1:
                    self._player1choice = choice
                else:
                    self._player2choice = choice
                self.switch_turn()
                return choice
            except ValueError:
                print("make sure you typed in a number!")

    def interpret_choice(self, choice):
        return self._choice_interpreter[choice]

    def draw_text(self):
        print("Draw! no one wins!")

    def playerwin(self, player):
        print(f"Player {player} Won!")

    def who_won(self):
        if self._player1choice == self._player2choice:
            return self.draw_text()
        elif self._player1choice == 0:
            if self._player2choice == 1:
                self.playerwin(2)
            else:
                self.playerwin(1)

        elif self._player1choice == 1:
            if self._player2choice == 2:
                self.playerwin(2)
            else:
                self.playerwin(1)

        else:
            if self._player2choice == 0:
                self.playerwin(2)
            else:
                self.playerwin(1)

    def announcement(self):
        print(f"player 1 chose {self.interpret_choice(self._player1choice)}")
        print(f"player 2 chose {self.interpret_choice(self._player2choice)}")
        print("The result is...")
        self.who_won()


    def generate_round(self):
        if self._player_turn == 1:
            self.generate_player()
            if self._computer_opponent:
                self.generate_computer()
            else:
                self.generate_player()
            self.announcement()
        else:
            pass # some error that the game needs to be reset


if __name__ == '__main__':
    print("welcome to Rock Paper Scissors")
    new_game = RockPaperScissors("false")
    new_game.generate_round()