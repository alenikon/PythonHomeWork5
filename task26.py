# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


def stepen(a, b):
    if b == 1:
        return a
    elif b % 2 == 0:
        rez = stepen(a, b // 2)
        return rez*rez
    else:
        rez = stepen(a, b // 2)
        return rez*rez*a
print('Результат: ', stepen(int(input('Введите число: ')), int(input('Введите число степень: '))))