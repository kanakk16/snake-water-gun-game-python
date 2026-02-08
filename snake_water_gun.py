import random
'''
snake: 0
water: 1
gun: -1
'''
computer = random.choice([0, 1, -1])

print("s for Snake.\nw for Water.\ng for Gun.")
yourstr = input("Enter your choice: ").lower()

yourdict = {"s": 0,
           "w": 1,
           "g": -1}

reversedict = {0: "Snake",
               1: "Water",
               -1: "Gun"}

if yourstr not in yourdict:
    print("Invalid Input!!")
    exit()

you = yourdict[yourstr]

print(f"You choose: {reversedict[you]}\nComputer choose: {reversedict[computer]}")
if(computer == you):
    print("It is Draw!!")
elif(computer == 0 and you == -1) or\
    (computer == 1 and you == 0) or\
    (computer == -1 and you == 1):
    print("You Win!!")
else:
    print("You Lose!!")
