import math
import random


def main():
    print("\nWelcome to Brain Games!")
    player_name = input("What is your name? ").strip()
    print(f"\nHello, {player_name}!")
    print("\nGame 1: Least Common Multiple")
    print("Find the LCM of three numbers")
    play_lcm_game(player_name)
    print("\nGame 2: Geometric Progression")
    print("Find the missing number in the sequence")
    play_progression_game(player_name)


def play_lcm_game(name):
    rounds = 3
    for _ in range(rounds):
        numbers = [random.randint(1, 50) for _ in range(3)]
        solution = lcm_of_three(*numbers)
        print(f"\nNumbers: {numbers[0]}, {numbers[1]}, {numbers[2]}")
        guess = input("Your answer: ").strip()
        if not guess.isdigit():
            print("Please enter a valid number")
            continue
        if int(guess) == solution:
            print("Correct!")
        else:
            print(f"Incorrect. The right answer was {solution}.")
            print(f"\nGame over, {name}. Try again later.")
            return
    print(f"\nCongratulations, {name}! You won the LCM game.")


def lcm_of_three(a, b, c):
    def lcm(x, y):
        return x * y // math.gcd(x, y)

    return lcm(lcm(a, b), c)


def play_progression_game(name):
    rounds = 3
    for _ in range(rounds):
        start = random.randint(1, 5)
        ratio = random.randint(2, 4)
        length = random.randint(7, 10)
        progression = [start * (ratio**i) for i in range(length)]
        hidden_index = random.randint(2, length - 3)  # Keep middle positions
        answer = progression[hidden_index]
        progression[hidden_index] = ".."
        print("\nProgression:", " ".join(map(str, progression)))
        guess = input("Missing number: ").strip()
        if not guess.isdigit():
            print("Please enter a valid number")
            continue
        if int(guess) == answer:
            print("Correct!")
        else:
            print(f"Wrong. The correct answer was {answer}.")
            print(f"\nGame over, {name}. Try again later.")
            return
    print(f"\nWell done, {name}! You mastered the progression game.")


if __name__ == "__main__":
    main()
