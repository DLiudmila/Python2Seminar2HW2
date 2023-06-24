# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.


# Суммируем дроби
def fraction_sum(fraction1, fraction2):
    # Разбиваем строки на числитель и знаменатель
    num1, den1 = map(int, fraction1.split("/"))
    num2, den2 = map(int, fraction2.split("/"))
    sum_num = num1 * den2 + num2 * den1
    sum_den = den1 * den2
    return f"{sum_num}/{sum_den}"


# Произведение дробей
def fraction_mul(fraction1, fraction2):
    # Разбиваем строки на числитель и знаменатель
    num1, den1 = map(int, fraction1.split("/"))
    num2, den2 = map(int, fraction2.split("/"))
    mul_num = num1 * num2
    mul_den = den1 * den2
    return  f"{mul_num}/{mul_den}"


fraction1 = input('Ведите первую дробь(пример: 1/5): ')
fraction2 = input('Ведите вторую дробь(пример: 1/5): ')
sum_result = fraction_sum(fraction1, fraction2)
mul_result = fraction_mul(fraction1, fraction2)
print(f"Сумма: {sum_result}")
print(f"Произведение: {mul_result}")