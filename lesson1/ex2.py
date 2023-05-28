number = int(input('Введите число: '))

print('Сумма цифр:', number%10 + number//100 + number%100//10)