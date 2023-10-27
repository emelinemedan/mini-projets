import random
print("1: Lancer le dé, 0: Quitter le programme")
while True:
    # the user is asked to choose a number
    x=int(input("press a number "))
    if x==0:
        print("Bye, see you later !")
        break
    elif x==1 :
        print(random.randint(1, 6))
    else:
        print("press 0 to stop or 1 to continue")