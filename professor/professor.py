from game import ask_positive_number
import random


def main():
    score = 0

    level = get_level()

    for i in range(10):
        score += generate_and_solve_math_problem(level)
    
    print(f"Your score: {score}")


def get_level():
    levels = [1, 2, 3]
    while True:
        level = ask_positive_number("Level: ")
        if level in levels:
            return level


def generate_integer(level):
    mins = {1: 1, 2: 10, 3: 100}
    maxs = {1: 9, 2: 99, 3: 999}
    if level not in mins:
        raise ValueError

    return random.randint(mins[level], maxs[level])

def generate_and_solve_math_problem(level):
    x = generate_integer(level)
    y = generate_integer(level)

    answer = str(x + y)

    attempts = 0

    while attempts < 3:
        response = input(f"{x}+{y}=")
        if response == answer:
            return 1
        
        attempts += 1
        print("EEE")
    
    print(answer)
    return 0

if __name__ == "__main__":
    main()