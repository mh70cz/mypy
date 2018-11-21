"""
Bite 42. Number Guessing Game Class 

https://codechalleng.es/bites/42
"""
 
MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses =  set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        guess = input('Please enter a number')
        try:
            guess = int(guess)
        except:
            raise ValueError("Please enter a number")
        if not (START <= guess <= END):
            raise ValueError("Number not in range")
        if guess in self._guesses:
            raise ValueError("Already guessed")
        self._guesses.add(guess)
        return guess

    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        if guess == self._answer:
            print(f"{guess} is correct!")
            return True
        if guess < self._answer:
            print(f"{guess} is too low")
            return False
        if guess > self._answer:
            print(f"{guess} is too high")

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        while len(self._guesses) < MAX_GUESSES:
            try:
                valid = self._validate_guess(self.guess())
                if valid:
                    print(f'It took you {len(self._guesses)} guesses')
                    self._win = True
                    return
                else:
                    continue
            except ValueError as e:
                msg = e.args[0]
                print(msg)
                continue
        print(f"Guessed {len(self._guesses)} times, answer was {self._answer}")
        


#if __name__ == '__main__':
#    game = Game()
#    game()



from unittest.mock import patch
import random

import pytest




@patch.object(random, 'randint')
def test_get_random_number(m):
    m.return_value = 17
    assert get_random_number() == 17


@patch("builtins.input", side_effect=[11, '12', 'Bob', 12, 5, -1, 21, 7, None])
def test_guess(inp):
    game = Game()
    # good
    assert game.guess() == 11
    assert game.guess() == 12
    # not a number
    with pytest.raises(ValueError):
        game.guess()
    # already guessed 12
    with pytest.raises(ValueError):
        game.guess()
    # good
    assert game.guess() == 5
    # out of range (x2)
    with pytest.raises(ValueError):
        game.guess()
    with pytest.raises(ValueError):
        game.guess()
    # good
    assert game.guess() == 7
    # hitting enter / no input
    with pytest.raises(ValueError):
        game.guess()


def test_validate_guess(capfd):
    """pytest capture stdout:
       https://docs.pytest.org/en/2.9.1/capture.html"""
    game = Game()
    game._answer = 2

    assert not game._validate_guess(1)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '1 is too low'

    assert not game._validate_guess(3)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '3 is too high'

    assert game._validate_guess(2)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '2 is correct!'


@patch("builtins.input", side_effect=[4, 22, 9, 4, 6])
def test_game_win(inp, capfd):
    game = Game()
    game._answer = 6

    game()
    assert game._win is True

    out, _ = capfd.readouterr()
    expected = ['4 is too low', 'Number not in range',
                '9 is too high', 'Already guessed',
                '6 is correct!', 'It took you 3 guesses']

    output = [line.strip() for line in out.split('\n') if line.strip()]
    for line, exp in zip(output, expected):
        assert line == exp


@patch("builtins.input", side_effect=[None, 5, 9, 14, 11, 12])
def test_game_lose(inp, capfd):
    game = Game()
    game._answer = 13

    game()
    assert game._win is False

    out, _ = capfd.readouterr()
    expected = ['Please enter a number', '5 is too low',
                '9 is too low', '14 is too high',
                '11 is too low', '12 is too low',
                'Guessed 5 times, answer was 13']

    output = [line.strip() for line in out.split('\n') if line.strip()]
    for line, exp in zip(output, expected):
        assert line == exp

import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          
    
#python -m pytest xxx_test.py
    