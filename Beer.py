#Programer: Gabriel Hart
#Last revision: 3/4/22
x=input("How many bottles?")
try:
    x=int(x)
except:
    print("You may have had too many already!")
    x=-1
if x>99:
    print("Are you trying to pickle your liver?")
elif x<1:
    print("Why don't you have any beer?")
elif x>1:
    while x>1:
        y=str(x)
        print(y + " bottles of beer on the wall,")
        print(y + " bottles of beer,")
        print("take one down and pass it around,")
        if (x-1)>1:
            z=str(x-1)
            print(z + " bottles of beer on the wall!")
        else:
            z=str(x-1)
            print(z,"bottle of beer on the wall!")
        print("")
        x=x-1
elif x==1:
    print("1 bottle of Beer on the wall")
    print("1 bottle of beer,")
    print("take one down and pass it around,")
print("Now the party's over!")
