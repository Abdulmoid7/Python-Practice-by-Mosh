import random

for i in range(3):
    print(random.randint(10, 20))

members = ['Moid', 'Mahrukh', 'Huzaifa', 'Murtuza']
leader = random.choice(members)
print(leader)

dice1 = ['1', '2', '3', '4', '5', '6']
dice2 = ['1', '2', '3', '4', '5', '6']

result1 = random.choice(dice1)
result2 = random.choice(dice2)
leader = random.choice(result1, result2)
print(leader)