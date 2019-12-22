# Калькулятор Физики v0.2.0


import re
m = 0
lambda_x = 0
# formul_ytp = m * lambda_x
formulmatch_ytp = 0
testing_for_kg = 0
given_str_number = []
given_str = []
regiven_str = []

def given(number_string):
    global given_str, given_str_number, regiven_str, testing_for_kg, m, lambda_x, formulmatch_ytp
    i = 0
    print("Дано:\n")
    while i < number_string:
        
        given_str.append(input())
        regiven_str.append(given_str[i].replace(' ', ''))
        given_str[i] = given_str[i].replace("**", ' ')
        given_str[i] = given_str[i].replace("*", ' ')
        given_str_number.append(find_num(given_str[i]))


        i += 1

    cls(100)
    def formule():
        j = 0
        while j < len(given_str_number):
            global formulmatch_ytp, lambda_x, m
            if 'lambda=' in regiven_str[j]:
                lambda_x = given_str_number[j]
                formulmatch_ytp += 1
            if 'm=' in regiven_str[j]:
                m = given_str_number[j]
                formulmatch_ytp += 1
            j += 1
        lambda_x = ''.join(lambda_x)
        m = ''.join(m)
    formule()
    
    def SI():
        global formulmatch_ytp, lambda_x, m, testing_for_kg
        j = 0
        while j < len(given_str):
            if 'тонн' in given_str[j] or 'т' in given_str[j]:
                m = float(m) * 1000
                testing_for_kg = 1
            elif 'гр' in given_str[j] or 'gr' in given_str[j]:
                m = float(m) / 1000
                testing_for_kg = 1
            else:
                pass
            j += 1
    
        def result():
            if formulmatch_ytp == 2:
                
                result_ytp = float(m) * float(lambda_x)
                j = 0
                while j < len(given_str):
                    if given_str[j] == '':
                        del(given_str[j])
                        j -= 1
                    else:
                        j += 1
                    print("Дано:\n{0}".format('\n'.join(given_str)))
                    print("СИ:\n{0} kg".format(m))
                    if result_ytp > 1000000:
                        print("Решение:\nQ = lambda*m\nQ = {0} Дж/Кг * {1} кг = {2} Дж = {3} МДж\nОтвет: Q = {3} МДж.".format(lambda_x, m, result_ytp, result_ytp / 1000000))
                    elif result_ytp > 5000:
                        print("Решение:\nQ = lambda*m\nQ = {0} Дж/Кг * {1} кг = {2} Дж = {3} КДж\nОтвет: Q = {3} КДж.".format(lambda_x, m, result_ytp, result_ytp / 1000))
                    else:
                        print("Решение:\nQ = lambda*m\nQ = {0} Дж/Кг * {1} кг = {2}\nОтвет: Q = {2} Дж.".format(lambda_x, m, result_ytp))
        result()
    SI()
    
def cls(clsed):
    print("\n" * clsed)
def find_num(input_str): # Сам алгоритм, внизу всё, что происходит для извлечения числа.
#               ↑
#          Параметр input_str - это строка, из которой, мы будем извлекать числа.
#
    numbers = [] # Список, в который мы будем записывать числа, извлеченные из строки.
    input_str = re.split(' ', input_str) # Предложение делим на слова,
#                                        таким образом создаём список
    i = len(input_str) # Узнаём размер нашей строки - input_str
#    Тоесть, считаем каждое слово. Сколько слов, такой и размер строки.
    j = 0 # создаём переменную для цикла (номер для списка)
#    Logic Functions / В этом цикле и происходит извлечение чисел из строки.
    while j != i: # Пока j, не будет равно i. j это номер списка,
        #                                              i - это размер строки.
        # Простыми словами, цикл будет длиться, пока слова не закончаться.
        out_number = '' # Создаём пустой объект.
        for element in input_str[j]: # цикл проверки "это буква? если нет, то добавляем в число"
#                                                                 если да, то выходим из цикла
#
#                                 например a4: a - это буква, не будем её включать в число,
#                                              4 - это цифра, будем включать её в число. 
#
            if (element == '.' and '.' not in out_number) or element.isdigit(): # Если это цифра или точка, 
                out_number += element                                           # то добавляется в число out_number
            elif out_number: #                                                    иначе, если условие не сработало
                break #                                                           то мы выходим из цикла
#                                                                               (Всё, о чём мы говорили выше)
        if out_number == '.': # если, наше число это просто точка, без цифр
            out_number = ' '  #                                    то, удаляем её
        else:
            numbers.append(out_number) # У нас получилось число! Добавляем его в список чисел.
        j += 1 # Номер для списка, увеличиваем на один, то есть переходим к следующему слову,
#                                                      чтобы также проверить его на наличие цифр
#           Незабываем, что это цикл и он будет повторяться несколько раз до того, когда слова закончаться!
#      Если слова закончились, то цикл завершается
    numbers = list(filter(None, numbers)) # Стираются пробелы, это просто мусор для нашего списка
    return numbers # Алгоритм завершён, числа, если они есть извлеклись из строки и добавились в список numbers!
while True:  
    a = input("1. Начать писать через дано. \n ") 
    if a == '1':
        m = 0
        lambda_x = 0
        # formul_ytp = m * lambda_x
        formulmatch_ytp = 0
        testing_for_kg = 0
        given_str_number = []
        given_str = []
        regiven_str = []
        
        given(6)

        
    elif a == 'EXIT' or 'Exit' or 'exit' or 'CLOSE' or 'Close' or 'close' or 'Закрыть' or 'K':
        break

            


