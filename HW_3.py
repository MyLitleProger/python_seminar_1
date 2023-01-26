# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# Пример:
# 385916 -> yes
# 123456 -> no

# ввод данных
#number = 385916
number = int(input('Введите число: '))

# работа с данными
# int отбрасывает окончание числа оставляя только целую часть
# round округляет число до целого
one = int(number / 100000)                      # 385916 / 100000 -> 3,85916
two = int(((number / 100000) % 1) * 10)         # 385916 / 100000 -> 3,85916 % 1 -> 0,85916 * 10 -> 8,5916
three = int(((number / 10000) % 1) * 10)        # 385916 / 10000 -> 38,5916 % 1 -> 0,5916 * 10 -> 5,916
four = int(((number / 1000) % 1) * 10)          # 385916 / 1000 -> 385,916 % 1 -> 0,916 * 10 -> 9,16
five = int(((number / 100) % 1) * 10)           # 385916 / 100 -> 3859,16 % 1 -> 0,16 * 10 -> 1,6
# после 5-го элемента питон выдает 5.999999999985448 по этому воспользуюсь функцией round
six = round(((number / 10) % 1) * 10)           # 385916 / 10 -> 38591,6 % 1 -> 0,6 * 10 -> 6

first = one + two + three                       # сумма первый трех элементов
second = four + five + six                      # сумма последних трех элементов

if first == second:                             # проверка равтости элементов
    print(f'{number} -> yes')
else:
    print(f'{number} -> no')