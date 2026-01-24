import random

def roll_dice():
    max = int(input("How many sides are there to this dice? "))
    roll = random.randint(1, max)
    print(f"You have rolled {roll} on your {max}-sided dice")

roll_dice()