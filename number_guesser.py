
import random
import time


def mode_easy():
    lives = 4
    print('Yoo mate you have choose the easy mode. Guess number between 1 to 10')
    time.sleep(3)
    print('Picking Number ...')
    time.sleep(3)
    user_guess = int(input('What is your guess?: '))
    lives -= 1
    correct_answer = random.randint(1, 10)

    while user_guess != correct_answer:
        if user_guess > correct_answer:
            print(f'You have guess the higher. Now, your lives remain {lives}')
            user_guess = int(input('What is your guess?: '))
        elif user_guess < correct_answer:
            print(f'You have guess the lower. Now, your lives remain {lives}')
            user_guess = int(input('What is your guess?: '))

        if lives == 1:
            print(f'You lose. The correct guess was {correct_answer}')
            user_exit()
        lives -= 1
        
    if user_guess == correct_answer:
            print(f'You have guess the correct number {correct_answer}')
            user_exit()

def mode_normal():
    lives = 5
    print('Yoo mate you have choose the normal mode. Guess number between 1 to 50')
    time.sleep(3)
    print('Picking Number ...')
    time.sleep(3)
    user_guess = int(input('What is your guess?: '))
    lives -= 1
    correct_answer = random.randint(1, 50)

    while user_guess != correct_answer:
        if user_guess > correct_answer:
            print(f'You have guess the higher. Now, your lives remain {lives}')
            user_guess = int(input('What is your guess?: '))
        elif user_guess < correct_answer:
            print(f'You have guess the lower. Now, your lives remain {lives}')
            user_guess = int(input('What is your guess?: '))

        if lives == 1:
            print(f'You lose. The correct guess was {correct_answer}')
            user_exit()
        lives -= 1
        
    if user_guess == correct_answer:
            print(f'You have guess the correct number {correct_answer}')
            user_exit()

def mode_hard():
    lives = 6
    print('Yoo mate you have choose the hard mode. Guess number between 1 to 100')
    time.sleep(3)
    print('Picking Number ...')
    time.sleep(3)
    user_guess = int(input('What is your guess?: '))
    lives -= 1
    correct_answer = random.randint(1, 100)

    while user_guess != correct_answer:
        if user_guess > correct_answer:
            print(f'You have guess the higher. Now, your lives remain {lives}')
            user_guess = int(input('What is your guess?: '))
        elif user_guess < correct_answer:
            print(f'You have guess the lower. Now, your lives remain {lives}')
            user_guess = int(input('What is your guess?: '))

        if lives == 1:
            print(f'You lose. The correct guess was {correct_answer}')
            user_exit()
        lives -= 1
        
    if user_guess == correct_answer:
            print(f'You have guess the correct number {correct_answer}')
            user_exit()


def mode_cosm():
    print('Costom mode')
    try:
        lives = int(input('Enter how much lives do you want to access for guess: '))
        min = int(input('min number: '))
        max = int(input('maxnumber: '))
    except:
        print('Invalid input. Enter valid number.')
    
    print(f'Yoo mate you have choose the hard mode. Guess number between {min} to {max}')
    time.sleep(3)
    print('Picking Number ...')
    time.sleep(3)
    user_guess = int(input('What is your guess?: '))
    lives -= 1
    correct_answer = random.randint(min, max)

    while user_guess != correct_answer:
        if user_guess > correct_answer:
            print(f'You have guess the higher. Now, your lives remain {lives}')
            user_guess = int(input('What is your guess?: '))
        elif user_guess < correct_answer:
            print(f'You have guess the lower. Now, your lives remain {lives}')
            user_guess = int(input('What is your guess?: '))

        if lives == 1:
            print(f'You lose. The correct guess was {correct_answer}')
            user_exit()
        lives -= 1
        
    if user_guess == correct_answer:
            print(f'You have guess the correct number {correct_answer}')
            user_exit()
    

def user_exit():
    user_exit = input('Do you want to exit? (yes/no):').lower()
    if user_exit == 'yes':
        print('Bye! Fellow mate')
        exit
    else:
        print('You are great Player')
        guess_game()


def guess_game():
    print('--------------------------------------------------')
    print('|                                                |')
    print('|  Hello! fellow mate Welcome to the guess game  |')
    print('|                                                |')
    print('|          Enter easy for easy mode              |')
    print('|          Enter normal for normal mode          |')
    print('|          Enter hard for the hard mode          |')
    print('|          Enter Cosm for costom game            |')
    print('|                                                |')
    print('|                                                |')
    print('------------------------------------------------')
    game_mode = input('Enter the game mode: ').lower()

    if game_mode == 'easy':
        mode_easy()
    elif game_mode == 'normal':
        mode_normal()
    elif game_mode == 'hard':
        mode_hard()
    elif game_mode == 'cosm':
        mode_cosm()
    else:
        print('Fellow met you have enter the wrong input')
        guess_game()

guess_game()
