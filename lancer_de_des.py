import random
print("1: Lancer le dé, 0: Quitter le programme")
while True:
    #the user is asked to click on a number
    x=int(input("Press a number "))
    if x==0:
        print("bye, see you later")
        break
    elif x==1:
        print(random.randint(1,6))
    else:
        print("press 0 to stop or 1 to continue")