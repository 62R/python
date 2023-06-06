def find_min_max(list):
    min = list[0]
    max = list[0]
    for i in list:
        if i > max: 
            max = i
        if i < min:
            min = i
    return  [min, max]
      

n = int(input('Введите количество арбузов: '))
weightList = []

for i in range(n): 
    weightList.append(int(input()))


# weightList = [20, 30, 23, 45, 40, 50, 5, 10]

print(find_min_max(weightList))
        
    