dayCount = int(input('Введите количество дней: '))
maxPositiveDay = 0
currentPositiveDay = 0
tempList = []

for i in range(dayCount): 
    tempList.append(int(input()))


# tempList = [-20, 30, 23, 145, -40, 50, 10, -10]

for dayTemp in tempList:
    if dayTemp > 0:
      currentPositiveDay += 1
    else:
        if currentPositiveDay > maxPositiveDay:
            maxPositiveDay = currentPositiveDay
            currentPositiveDay = 0

print(maxPositiveDay)
        
    