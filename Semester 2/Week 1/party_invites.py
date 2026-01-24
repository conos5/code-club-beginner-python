# The Party Greeter

# 1. Taking number of guests
amount = int(input("How many people would you like to have at your birthday party?"))
print(f"Who are the {amount} people you want to invite? ")

# 2. Taking names
guests = []
count = 1
while count <= amount:
    guests.append(input(f"Friend {count}: "))
    count += 1


print("\n--- SENDING INVITES ---")

# 3. Use a loop to perform an action for every item
for person in guests:
    print(f"Sending email to: {person} ... Sent!")
    
print("All invites sent!")
