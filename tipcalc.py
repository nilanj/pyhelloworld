iString = input ('How many people are there? ')
i = int(iString)

tax = 1.07

meals=[]

for x in range(0,i):
    stringitem = input("How much was this persons meal on the menu?" )
    item = int(stringitem)
    meals.append(item)
    print(meals[x])

for x in range (0,i):
    meals[x] = meals[x] * tax

print(meals)

tips=[]

for x in range (0,i):
    tipamount = input('How much do you want to tip? ')
    tip = int(tipamount)/100
    tips.append(tip)

for x in range (0,i):
    meals[x] = meals[x] + meals[x]*tips[x]

for x in range (0,i):
    print("Person", x, "should pay", meals[x])



