#
# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0]
import random

size = int(input('Введите степень k многочлена: '))
koef = [0] * (size + 1)  # Размер многочлена с учётом элемента без x
for i in range(len(koef)):
    koef[i] = random.randint(0, 101)
equation = ''
print(koef)
for i in range(len(koef) - 1, -1, -1):
    if i == size:
        if koef[i] == 0:
            equation += ''
        elif koef[i] == 1:
            equation += f'x**{i}'
        else:
            equation += f'{koef[i]}*x**{i}'
    elif i == 0:
        if koef[i] == 0:
            equation += ''
        else:
            equation += f'+{koef[i]}'
    else:
        if koef[i] == 0:
            equation += ''
        elif koef[i] == 1:
            equation += f'+x**{i}'
        else:
            if i == 1:
                equation += f'+{koef[i]}*x'
            else:
                equation += f'+{koef[i]}*x**{i}'
print(equation)



