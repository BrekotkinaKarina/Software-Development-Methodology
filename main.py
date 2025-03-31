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
        numbers = generate_random_numbers(3, 1, 50)
        solution = lcm_of_three(*numbers)
        print(f"\nNumbers: {numbers[0]}, {numbers[1]}, {numbers[2]}")
        if not check_user_answer(solution):
            print(f"\nGame over, {name}. Try again later.")
            return
    print(f"\nCongratulations, {name}! You won the LCM game.")


def play_progression_game(name):
    rounds = 3
    for _ in range(rounds):
        progression, answer = generate_geometric_progression()
        print("\nProgression:", " ".join(map(str, progression)))
        if not check_user_answer(answer):
            print(f"\nGame over, {name}. Try again later.")
            return
    print(f"\nWell done, {name}! You mastered the progression game.")


def generate_random_numbers(count, min_val, max_val):
    """Генерирует список случайных чисел."""
    return [random.randint(min_val, max_val) for _ in range(count)]


def generate_geometric_progression():
    """Генерирует геометрическую прогрессию с пропущенным элементом."""
    start = random.randint(1, 5)
    ratio = random.randint(2, 4)
    length = random.randint(7, 10)
    progression = [start * (ratio**i) for i in range(length)]
    hidden_index = random.randint(2, length - 3)
    answer = progression[hidden_index]
    progression[hidden_index] = ".."
    return progression, answer


def check_user_answer(solution):
    """Проверяет ответ пользователя и возвращает True/False."""
    guess = input("Your answer: ").strip()
    if not guess.isdigit():
        print("Please enter a valid number")
        return False
    if int(guess) != solution:
        print(f"Incorrect. The right answer was {solution}.")
        return False
    print("Correct!")
    return True


def lcm_of_three(a, b, c):
    """Вычисляет НОК трёх чисел."""

    def lcm(x, y):
        return x * y // math.gcd(x, y)

    return lcm(lcm(a, b), c)


if __name__ == "__main__":
    main()
