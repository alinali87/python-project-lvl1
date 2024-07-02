import prompt
import random
from brain_games.cli import welcome_user
from brain_games.utils import congrat_user, is_prime


def calc_game(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct = 0
    while True:
        n = random.randint(1, 100)
        correct_answer = "yes" if is_prime(n) else "no"
        print(f"Question: {n}")
        a = prompt.string("Your answer: ")
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
