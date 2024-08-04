import random
target=random.randint(1,100)
while True:
    userChoice=int(input("Guess the target or QUIT(Q): "))
    if(userChoice=="Q"):
        break
    userChoice==int(userChoice)
    if(userChoice==target):
        print("Number Found!!")
        break
    elif(userChoice<target):
        print("Your number was too small.Take a bigger guess....")
    else:
        print("Your number was too big.Take a bigger guess....")

print("....GAME OVER....")