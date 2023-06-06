s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение: '))

x = int((s+int((s**2 - 4*p)**(0.5)))/2)
y =  s - x 

print(x, y)