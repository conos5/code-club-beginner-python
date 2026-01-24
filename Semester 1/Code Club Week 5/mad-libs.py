print("=== STORY GAME ===")

# Taking multiple inputs
noun = input("Give me a noun: (name of a thing - example: 'dog', 'computer')")
verb = input("Give me a verb: (an action - example: 'walk', 'run')")
adjective = input("Give me an adjective: (example: 'big', 'blue')")
place = input("Give me a place: ")

# Creating story with f-string
print(f"\nOnce upon a time, there was a {adjective} {noun}.")
print(f"It liked to {verb} in {place}.")
print(f"Everyone loved the {adjective} {noun}!")