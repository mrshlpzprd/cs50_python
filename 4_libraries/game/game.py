import random

def main():
    level_number = 1
    while True:
        level_number = input('Level: ')

        if level_number.isnumeric() and int(level_number) >= 1:
            try:
                random_number = random.randint(1, int(level_number))
                check_user_guess(random_number)
                break
            except ValueError:
                pass

def check_user_guess(random_number):
    user_guess = 1
    while True:
        user_guess = input('Guess: ')

        try:
            if user_guess.isnumeric():
                if int(user_guess) < random_number:
                    print('Too small!')
                elif int(user_guess) > random_number:
                    print('Too large!')
                else:
                    print('Just right!')
                    exit()
        except ValueError:
            pass

main()


