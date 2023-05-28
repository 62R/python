number = int(input('Введите номер билета: '))

if number%10+ number%100//10  + number%1000//100 == number%10000//1000  + number%100000//10000 + number//100000:
  print('yes')
else:
  print('no')