count = int(input('Введите количество журавликов: '))

petrValue = count // 6
kateValue = count // 6 * 4
sergValue = count // 6

if count % 6 == 0:
    print('Петя  %d Катя  %d  Сережа %d .' %(petrValue,kateValue,sergValue))
else:
    print('Петя  %d Катя  %d  Сережа %d учитель %d.' %(petrValue,kateValue,sergValue, count%6))