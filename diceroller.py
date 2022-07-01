import random

dice = input('Please enter the number of dice:')
sides = input('How many sides?')

for i in range(int(dice)):
    print(random.randint(1,int(sides)))
