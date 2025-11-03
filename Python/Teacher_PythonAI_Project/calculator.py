# КОНСОЛЬНИЙ КАЛЬКУЛЯТОР

number_1 = float(input('Введіть число: '))
operation = input('Введіть операцію(+, -, *, /): ')
number_2 = float(input('Введіть число: '))

if operation == "+":
    print(number_1 + number_2)
elif operation == '-':
    print(number_1 - number_2)
elif operation == '*':
    print(number_1 * number_2)
elif operation == '/':
    if number_2 != 0:
        print(number_1 / number_2)
    else:
        print('ERROR. На нуль ділити не можна!')
else:
    print('ERROR. Невідома операція!')
