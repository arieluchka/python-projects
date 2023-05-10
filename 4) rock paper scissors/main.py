import random

# write a limit that the player can choose how many games he can play
# make choosing the option NOT CASE SENSETIVE

# idea for later project = make rock paper scissors with sockets, to have 2 players againts each other.


def player_choice_and_validation():
    # control = 1
    while True:
        choice_input = input("Rock, Paper or scissors? \n")
        choice_input = choice_input.lower()
        if choice_input in ["rock", "paper", "scissors"]:
            return choice_input
        else:
            print("Error! make sure your input is correct. try again!")
            pass


def generate_computer():
    choice = random.randint(1, 3)
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    else:
        return "scissors"

# change from print to return
# 0 draw, 1 win, 2 lose
def did_the_player_win(player_option, computer_option):
    if player_option == computer_option:
        print("draw!")
    if player_option == "rock":
        if computer_option == "paper":
            print("you lost!") # return lose
        else:
            print("you won!") # return win
    if player_option == "paper":
        if computer_option == "scissors":
            print("you lost!") # return lose
        else:
            print("you won!") # return win
    if player_option == "scissors":
        if computer_option == "rock":
            print("you lost!") # return lose
        else:
            print("you won!") # return win






if __name__ == '__main__':
    print("welcome to Rock Paper Scissors")
    did_the_player_win(player_choice_and_validation(), generate_computer())
    did_the_player_win(player_choice_and_validation(), generate_computer())
    did_the_player_win(player_choice_and_validation(), generate_computer())