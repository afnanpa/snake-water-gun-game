'''
snake =1
water = -1
gun = 0
'''




import random

computer = random.choice([1,0,-1])
youstr = input("enter your choice:")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"Snake",-1:"Water",0:"Gun"}

you = youDict[youstr]
print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if (computer == you):
    print("its a draw")

else:
    if(computer == 1 and you == -1):
        print("you lose")
    elif(computer ==-1 and you ==1):
        print("you win")
    elif(computer ==1 and you==0):
        print("you win")
    elif(computer ==0 and you==1):
        print("you lose")
    elif(computer ==0 and you==-1):
        print("you win")
    elif(computer ==-1 and you==0):
        print("you lose")
    else:
        print("something went wrong")
    




      



