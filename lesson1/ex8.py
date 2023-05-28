n = int(input('Введите ширину шоколадки: '))
m = int(input('Введите длину шоколадки: '))
k = int(input('Введите количесто долек: '))

if (k%n == 0 or k%m == 0) and k < n*m:
  print('yes')
else:
  print('no')