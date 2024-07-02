import prompt
import random
from math import gcd
from brain_games.cli import welcome_user
from brain_games.utils import congrat_user


def calc_game(name):
    print('What number is missing in the progression?')
    correct = 0
    while True:
        n = random.randint(6, 12)
        start = random.randint(1, 10)
        step = random.randint(1, 7)
        nums = list(range(start, start + n * step + 1, step))
        skip = random.choice(range(n))
        correct_answer = nums[skip]
        nums[skip] = ".."
        print(f"Question: {' '.join(map(str, nums))}")
        try:
            a_str = prompt.string("Your answer: ")
            a = int(a_str)
        except ValueError as e:
            print(f"Got ValueError: {e}")
            a = a_str
        if a == correct_answer:
            correct += 1
            print("Correct!")
        else:
            print(f"'{a}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            correct = 0
        if correct == 3:
            return True


def main():
    name = welcome_user()
    if calc_game(name):
        congrat_user(name)


if __name__ == '__main__':
    main()
