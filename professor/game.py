import random

def main():
    number = ask_positive_number("Level: ")

    random_number = random.randint(1,number)

    while True:
        answer = ask_positive_number("Guess: ")
        if answer < random_number:
           print("Too small! ")
        elif answer > random_number:
            print("Too large! ")
        else:
            print("Just right! ")
            return 0



def ask_positive_number(prompt:str):
    n = -1
    while n < 0:
        n = int(input(prompt))
    return n

if __name__ == "__main__":
    main()