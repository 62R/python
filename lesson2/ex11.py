def check_fib_position(num):
    firstNum = 0
    secondNum = 1
    n = 1

    while firstNum < num:
        temp = firstNum
        firstNum = secondNum
        secondNum += temp
        n += 1

    if firstNum == num:
        print('Это %d число Фибоначчи'%n)
    else:
        print('-1')
    return n


a = int(input('Введите число: '))

print(check_fib_position(a))