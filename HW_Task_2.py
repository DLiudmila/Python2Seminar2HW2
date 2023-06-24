# Напишите программу, которая получает целое число и
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def int_to_hex_string(num):
   hex_chars = '0123456789abcdef' # символы, используемые в шестнадцатеричной системе счисления
   hex_string = ''
   if num == 0:
       hex_string = '0'
   elif num < 0:
       # если число отрицательное, преобразуем его в беззнаковое
       # num = (1 << 32) + num
        num=num.replace("-","")
   while num > 0:
       # делим число на 16 и получаем остаток
       remainder = num % 16
       # добавляем соответствующий символ к строке
       hex_string = hex_chars[remainder] + hex_string
       # делим число на 16, используя операцию целочисленного деления
       num //= 16
   return hex_string


num = int(input('Введите число: '))
hex_string = int_to_hex_string(num)
print('наши расчеты:', hex_string)
print('функция hex:', hex(num))