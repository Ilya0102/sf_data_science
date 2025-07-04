"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

def game_core_v3(number: int = 1) -> int:
    """Опираясь на больше/меньше сокращает диапазон генерации случайного числа
    сводя количесто попыток к минимуму
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    mindig = 1
    maxdig = 101

    while True:
        count+=1
        predict_number = np.random.randint(mindig, maxdig)
    
        if predict_number > number:
            maxdig = predict_number
        
        elif predict_number < number:
            mindig = predict_number+1
        
        elif predict_number == number:
            break 
    # Ваш код заканчивается здесь

    return count

if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
