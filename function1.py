ages = [10, 20, 30, 40]
income = [100, 200, 300, 400]

def calcAges(list):
    sum = 0
    for i in list:
        sum = sum + i

    return sum/len(list)

print(calcAges(income))

