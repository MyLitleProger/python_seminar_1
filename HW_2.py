# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# ввод данных
total_cranes = int(input('Сколько всего сделали журавликов: '))

# работа с данными
# Петя x1
# Сережа x1
# Катя (1 + 1 = 2 => * 2 = 4) -> x4
# в сумме выходит 6
# по этому число журавликов делим на 6 в соотношении
if total_cranes % 6 == 0:
    petya = int(total_cranes / 6)
    seryozha = int(total_cranes / 6)
    katya = int(total_cranes - (petya + seryozha))

    # вывод данных
    print(f'{total_cranes} -> {petya} + {katya} + {seryozha}')
else:
    # вывод данных
    print('кто то соврал')