import prompt
import random
from operator import add, sub, mul
from brain_games.cli import welcome_user
from brain_games.utils import congrat_user, op_to_string


def calc_game(name):
    print('What is the result of the expression?')
    correct = 0
    while True:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        op = random.choice([add, sub, mul])
        correct_answer = op(num1, num2)
        print(f"Question: {num1} {op_to_string(op)} {num2}")
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
            print(f"'{a}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return False
        if correct >= 3:
            return True


def main():
    name = welcome_user()
    if calc_game(name):
        congrat_user(name)


if __name__ == '__main__':
    main()
