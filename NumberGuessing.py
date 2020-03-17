import random
chance=0
user=0
comp=0
for i in range(0,5):
    while chance<5:
        user1=int(input("enter the your  number"))
        comp1=random.randint(0,2)
        print("the computer number is",comp1)
        if(user1 == comp1 ):
            user+=1
        else:
            comp+=1
        break
    chance+=1
if user>comp:
    print("congrates You won")
else:
    print("sorry you lost")
