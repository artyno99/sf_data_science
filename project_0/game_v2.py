import numpy as np

def random_predict(number:int=1) -> int:
    """Сначала устанавливаем любое random число, потом делим диапазон на 2
    и находим середину, которую используем для следующей попытки. И так сужаем
    область поиска пока не достигнем результата.
     
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    low = 1
    high = 100
    
    while True:
        count += 1
        predict = (low+high) // 2
        
        if predict == number:
            break
        elif number > predict:
            low = predict + 1
        else:
            high = predict - 1
    return(count)
print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): _description_

    Returns:
        int: _description_
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

# RUN
if __name__ == '__main__':
    score_game(random_predict)
