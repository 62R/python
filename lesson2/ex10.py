coins = []

n = int(input('Введите количество монеток: '))

for i in range(n): 
    coins.append(int(input()))

# coins = [1, 0, 1, 1, 0, 0, 0]

eagle = 0
tails = 0

for coin in coins:
    if coin == 0:
        eagle += 1
    else:
        tails += 1

if eagle < tails:
    print('Необходимо перевернуть %d монет'%eagle)
else:
    print('Необходимо перевернуть %d монет'%tails)
