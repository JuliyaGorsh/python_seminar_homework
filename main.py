
# Решите квадратное уравнение 5x2-10x-400=0 последовательно
# сохраняя переменные a, b, c, d, x1 и x2.

# a, b, c = 5, 20, -40
# discriminant = b**2 - 4 * a * c
# if discriminant > 0:
#     x1 = (-b + discriminant ** 0.5) / 2 / a
#     x2 = (-b - discriminant ** 0.5) / 2 / a
#     print(x1, x2)
#
# elif discriminant == 0:
#     x = -b / 2 / a
#     print(x)
# else:
#     print('Корней нет')


# Посчитайте сумму чётных элементов от 1 до n исключая кратные e. Используйте while и if.
# Попробуйте разные значения e и n.
#
# n = int(input('Введите n число: '))
# e = int(input('Введите e число: '))
# i = 0
# summa = 0
# while i < n:
#     if i % 2 == 0 and i % e != 0:
#         summa += i
#     i += 1
# print(summa)



# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

# year = int(input('Введите год: '))
# res = None
# if year % 4 == 0:
#     if year % 400 == 0:
#         res = 'Твой год високосный'
#     elif year % 100 == 0:
#         res = 'Твой год не високосный'
#     else:
#         res = 'Твой год високосный'
# else:
#     res = 'Твой год не високосный'
# print(res)


# Пользователь вводит число от 1 до 999.
# Используя операции с числами сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25 Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число Откажитесь от магических чисел
# В коде должны быть один input и один print

# n = 0
# res = None
# while n < 1 or n >= 1000:
#     n = int(input('Введите число от 1 до 999: '))
#
# if n < 10:
#     res = n**2
# elif n >= 10 and n < 100:
#     a = n // 10
#     b = n % 10
#     res = a * b
# elif n >= 100 and n < 1000:
#     a = n // 100
#     b = n // 10 % 10
#     c = n % 10
#     res = c * 100 + b * 10 + a
# else:
#     res = 'Введите число из диапазона'
# print(res)

# __________________________________________

# message = None
#
# while not message:
#     number = int(input('Введите число: '))
#     if 0 < number < 10:
#         number = number ** 2
#         message = f'Однозначное - {number}'
#     elif 10 <= number < 100:
#         message = f'Двухзначное - {(number % 10) * (number // 10)}'
#     elif 100 <= number < 1000:
#         a, b, c = number // 100, number // 10 % 10, number % 10
#         message = f'Трехзначное - {a + b * 10 + c * 100}'
# print(message)


# Сколько рядов у елки?
# *
# ***
# *****
# ******
# *********
# num = int(input('Сколько рядов у елки? '))
# chr_tree_width = num * 2 - 1
# stars = 1
#
# for i in range(num):
#     print(f"{' '* (num - 1)}{'*' * stars}")
#     stars += 2
#     num -= 1

# num = int(input('Введите высоту елки: '))
#
# for i in range(num):
#     print(f'{"*"*(2*i+1):.^{(num*2-1)}}')



# Выведите в консоль таблицу умножение от 2х2 до 9х10 как на школьной тетрадке

res = [i for i in range(2, 11)]
for i in range(2, 11):
    for j in range(2, 11):
        print(f'{i} * {j} = {i*j}')

for j in range(2, 11):
    for i in range(2, 6):
        # print(f'{j} Х {i} = {j*i}', end='\t\t\t')
        print(f'{i:^3} Х {j:^3} = {j * i:^3}', end='\t\t\t')
    print()
print()
for j in range(2, 11):
    row = []
    for i in range(6, 10):
        # print(f'{j} Х {i} = {j*i}', end='\t\t\t')
        # print(f'{i:^3} Х {j:^3} = {j * i:^3}', end='\t\t\t')
        row.append(f'{i:^3} Х {j:^3} = {j * i:^3}')
    print('\t\t\t'.join(row))


for k in [0,1]:
    for j in range(2, 11):
        row = []
        for i in range(2+k*4, 6+k*4):
            row.append(f'{i:^3} Х {j:^3} = {j * i:^3}')
        print('\t\t\t'.join(row))
    print('\n')


# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c — стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


# a = int(input('Сторона a: '))
# b = int(input('Сторона b: '))
# c = int(input('Сторона c: '))
#
# if a > b + c or b > c + a or c > a + b:
#     print('Треугольник не существует')
# elif a == b and b == c:
#     print('Треугольник равносторонний')
# elif a == b or b == c or a == c:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')



# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу и на себя».
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.



# number = int(input('Введите число: '))
# count = 1
# res = 0
# if number > 0 and number < 100001:
#     while count < number+1:
#         if number % count == 0:
#             res = res + 1
#         count += 1
#     if res == 1:
#         print('1 - ни простое ни составное число')
#     elif res == 2:
#         print('Число простое')
#     else:
#         print('Число составное')
# else:
#     print('Введите числа от 1 до 100000')





# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
#
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

# from random import randint
# num = randint(0, 1000)
# print(num)
# count = 0
#
# while count < 10:
#     find = int(input('Введите загаданное число: '))
#     if find == num:
#         print('Ты угадал! Это число', num)
#         break
#     elif count == 9 and find != num:
#         print('Ты не угадал, попытки закончились')
#     elif find < num:
#         print('Загаданное число больше, попробуй еще раз')
#     elif find > num:
#         print('Загаданное число меньше, попробуй еще раз')
#
#     count += 1