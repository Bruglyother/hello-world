#Programer: Gabriel Hart
#Last revision: 7/1/22
''' This will be a remake of my original Beer file.'''

def chorus(bottles):
    print(str(bottles) + " bottles of beer on the wall,")
    print(str(bottles) + " bottles of beer,")
    print("take one down and pass it around,")
    if (bottles - 1) == 1:
        print("1 bottle of beer on the wall!")
        print('')
        print("1 bottle of Beer on the wall")
        print("1 bottle of beer,")
        print("take one down and pass it around,") 
    else:
        print(str(bottles - 1) + ' bottles of beer on the wall!')
        print('')
        chorus((bottles-1))

bottles=input("How many bottles?")
while True:
    try:
        bottles = int(bottles)
    except:
        print('You may have had too many already!')
        break
    if bottles > 99:
        print('Are you trying to pickle your liver?')
        break
    elif bottles < 1:
        print ('Why don;t you have any beer?')
        break
    else:
        chorus(bottles)
        break
print('Now the party is done!')