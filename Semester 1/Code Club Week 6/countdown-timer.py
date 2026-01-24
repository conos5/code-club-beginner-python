import time
print("=== COUNTDOWN TIMER ===")

number = int(input("Count down from what number? "))

while number > 0:
    print(number)
    number = number - 1
    # time.sleep(1) # ask them what this does
    
print("🚀 Blast off!")
