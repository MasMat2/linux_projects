foods = {'bars':[240, 400, 900], 'chips':[135, 400, 650], 'beef': [2800, 1500, 5000], 'almonds': [410, 410, 950], 'apples': [182, 190, 95]}
foods10 = {} # 10 is for the ten calories
foodYield = {}

for item in foods:
    dividend = foods[item][2]/10
    newValues = []
    for num in foods[item]:
        newValues.append(str(round(num/dividend, 2)))
    foods10[item] = newValues


for item in foods10:
    foodYield[item] = str(round(float(foods10[item][1]) + float(foods10[item][0]), 2))
    foods10[item][2] = str(10)

for item in foods10:
    print('  ' + item.ljust(10, '-') + foods10[item][0].center(10) + foods10[item][1].ljust(6) + foods10[item][2].ljust(6))

print()
print()
for item in foods10:
    print('  ' + item.ljust(10, '-') + foodYield[item].center(10) + foods10[item][2].ljust(6))
