import random

play_again = "y"

while play_again == "y":
    player = int(input("Pick heads (0) or tails (1): "))
    coin = random.randint(0, 1)
    
    if player == coin:
        print("🎉 You win!")
    else:
        print("😔 You lose!")
    
    play_again = input("Play again? (y/n): ")

print("Thanks for playing!")
