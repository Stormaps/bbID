string = input('Input text: ') # Вводим строку
string_reversed = ''.join(reversed(string)) # Переворачиваем её
if string == string_reversed: # Если перевёрнутая строка равна неперевёрнутой
    print("Yes, it's a palindrome") # Выводит на экран - Да, это палиндром
else: # Иначе, выводит - Нет, это не палиндром
    print("No, it's not a palindrome")
