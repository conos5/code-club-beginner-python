import random

# Taking input for player choice
player = int(input("Pick heads (0) or tails (1): "))

# Picking computer choice randomly
coin_flip = random.randint(0,1)

if player == coin_flip:
    print("You win")
else:
    print("You lose")




