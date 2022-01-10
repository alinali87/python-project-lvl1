#!/usr/bin/env python
from brain_games.cli import (
    welcome_user,
    start_game,
    congratulate,
    game_over
)
from random import randint


def main():
    name = welcome_user()
    start_game()
    counter = 0
    while counter < 3:
        num = randint(1, 100)
        print(f"Question: {num}")
        answer = input('Your answer: ')
        if (num % 2 == 0 and answer == 'yes') \
                or (num % 2 == 1 and answer == 'no'):
            print('Correct!')
            counter += 1
        else:
            game_over(name, answer, num)
            return
    congratulate(name)


if __name__ == '__main__':
    main()
