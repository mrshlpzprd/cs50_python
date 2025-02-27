import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        X, Y = generate_integer(level)
        for _ in range(3):
            answer = input(f'{X} + {Y} = ')
            if answer.isnumeric() and int(answer) == (X + Y):
                score += 1
                break
            else:
                print('EEE')
        else:
            print(f'{X} + {Y} = {X+Y}')
    print(f'Score: {score}')

def get_level():
    while True:
        level = input('Level: ')
        if level.isnumeric() and (1 <= int(level) <= 3):
            return int(level)

def generate_integer(level):
    num_range = [40*pow(level,2)+(-110*level)+70, int('9' * level)]
    X = random.randint(num_range[0], num_range[1])
    Y = random.randint(num_range[0], num_range[1])
    return X, Y

if __name__ == "__main__":
    main()
