import re

# Функция, которая находит числа.
def find_num(input_str): # Параметр input_str - это строка, из которой, мы будем извлекать числа.
    numbers = [] # Список, в который мы будем записывать числа, извлеченные из строки.
    input_str = re.split(' ', input_str) # Предложение делим на слова,
    #                                      таким образом создаём список
    i = len(input_str) # Узнаём lenght параметра input_str
    j = 0 # создаём переменную для цикла (номер для списка)
    
    # Logic Functions / В этом цикле и происходит извлечение чисел из строки.
    while j != i:
        if not input_str[j] and not isinstance(input_str[j], str):
            return 0
        out_number = ''
        for element in input_str[j]:
            if (element == '.' and '.' not in out_number) or element.isdigit():
                out_number += element
            elif out_number:
                break
        if out_number == '.':
            out_number = ' '
        else:
            numbers.append(out_number)
        j += 1
    numbers = list(filter(None, numbers)) # Стираются пробелы
    return numbers # Возвращаем наш список

string = input() # Даём пользователю ввести строку.
nums = find_num(string) # Вызываем нашу функцию извлечения чисел.
for i, item in enumerate(nums): 
    nums[i] = float(item) # преобразовываем каждый элемент списка во Float
print(nums)