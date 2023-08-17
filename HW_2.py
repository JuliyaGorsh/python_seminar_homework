
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите число: '))
num1 = num
res = ""
ost = ''
while num > 0:
    ost = num % 16
    if ost == 10:
        ost = 'A'
    elif ost == 11:
        ost = 'B'
    elif ost == 12:
        ost = 'C'
    elif ost == 13:
        ost = 'D'
    elif ost == 14:
        ost = 'E'
    elif ost == 15:
        ost = 'F'

    res = str(ost) + res
    num //= 16

print(f'Шестнадцатеричное представление числа {num} -', res)
print(f'С помощью функции hex -', hex(num1).replace("0x", ''))


#
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

# numerator - числитель
# denominator - знаменатель


# import fractions
#
# def str_to_list(num):
#     numbers = ''.join(i if i.isdigit() else ' ' for i in num).split()
#     for i in range(len(numbers)):
#         numbers[i] = int(numbers[i])
#     return numbers
#
# def summa(number1, number2):
#     result = [number1[0] + number2[0], number1[1]]
#     return result
#
# def summas(number1, number2):
#     new_denominator = number1[1] * number2[1]
#     new_numerator1 = new_denominator / number1[1] * number1[0]
#     new_numerator2 = new_denominator / number2[1] * number2[0]
#     result = new_numerator1 + new_numerator2
#     summ_fraction = [result, new_denominator]
#     return summ_fraction
#
# def printing(num1, num2, sign, frac):
#     i = 0
#     if frac[0] % frac[1] == 0:
#         result = frac[0] / frac[1]
#         print(f"{sign[0]} дробей: {num1}{sign[1]}{num2} = ", int(result))
#     else:
#         while frac[0] - i != 1:
#             if frac[0] % (frac[0] - i) == 0 and frac[1] % (frac[0] - i) == 0:
#                 result = [frac[0] / (frac[0] - i), frac[1] / (frac[0] - i)]
#                 print(f"{sign[0]} дробей: {num1}{sign[1]}{num2} = ", int(result[0]), '/', int(result[1]), sep='')
#                 break
#             i+=1
#         else:
#             print(f"{sign[0]} дробей: {num1}{sign[1]}{num2} = ", int(frac[0]), '/', frac[1], sep='')
#
# def multiplication(number1, number2):
#     fraction_multi = [number1[0] * number2[0], number1[1] * number2[1]]
#     return fraction_multi
#
# def fraction(number1, number2):
#     one = fractions.Fraction(int(number1[0]), int(number1[1]))
#     two = fractions.Fraction(int(number2[0]), int(number2[1]))
#     print("Сложение дробей с модулем fractions:", one + two)
#     print("Произведение дробей с модулем fractions:", one * two)
#
#
# one = input('Введите первую дробь в формате a/b: ')
# two = input('Введите вторую дробь в формате a/b: ')
# print()
# sign1 = ['Сложение', ' + ']
# sign2 = ['Произведение', ' * ']
#
# num_one = str_to_list(one)
# num_two = str_to_list(two)
#
# if num_one[1] == num_two[1]:
#     printing(one, two, sign1, summa(num_one, num_two))
# else:
#     printing(one, two, sign1, summas(num_one, num_two))
# printing(one, two, sign2, multiplication(num_one, num_two))
#
# print()
# fraction(num_one, num_two)


