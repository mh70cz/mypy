"""
Bite 93. Rock-paper-scissors and generator's send 


https://codechalleng.es/bites/093
"""

from random import choice

defeated_by = dict(paper='scissors',
                   rock='paper',
                   scissors='rock')
lose = '{} beats {}, you lose!'
win = '{} beats {}, you win!'
tie = 'tie!'


def _get_computer_move():
    """Randomly select a move"""
    return choice(list(defeated_by))


def _get_winner(computer_choice, player_choice):
    """Return above lose/win/tie strings populated with the
       appropriate values (computer vs player)"""
    if computer_choice == player_choice:
        return "tie"
    if defeated_by[player_choice] == computer_choice :
        return "lose"
    return "win"

def game():
    """Game loop, receive player's choice via the generator's
       send method and get a random move from computer (_get_computer_move).
       Raise a StopIteration exception if user value received = 'q'.
       Check who wins with _get_winner and print its return output."""
    welcome_message = "Welcome to Rock Paper Scissors"
    usr = yield (welcome_message)
    while True:
        if usr in ["quit", "q"]:
            break
        usr = usr.lower()
        if usr not in ["rock", "paper", "scissors"]:
            raise ValueError
        
        cmp = _get_computer_move()
        game_result = _get_winner(cmp, usr)
        if game_result == "tie":
            print(tie)
            usr = yield()
            continue
        if game_result == "lose":
            message = lose.format(cmp, usr)
        else:
            message = win.format(usr,cmp)
        print(message)
        usr = yield()