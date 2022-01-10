def welcome_user():
    import prompt
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def start_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def congratulate(name):
    print(f'Congratulations, {name}!')


def game_over(name, answer, num):
    if num % 2 == 0:
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
    print(f"Let's try again, {name}!")
