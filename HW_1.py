
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