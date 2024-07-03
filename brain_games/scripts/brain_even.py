import prompt
import random
from brain_games.cli import welcome_user
from brain_games.utils import congrat_user


def even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct = 0
    while True:
        num = random.randint(1, 100)
        correct_answer = "yes" if num % 2 == 0 else "no"
        print(f"Question: {num}")
        a = prompt.string("Your answer: ")
        if a == correct_answer:
            print("Correct!")
            correct += 1
        else:
            print(f"'{a}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}")
            return False
            # correct = 0
        if correct >= 3:
            congrat_user(name)
            return True


def main():
    even_game()


if __name__ == '__main__':
    main()
