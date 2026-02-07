tasks = []

pet = input("What is your pets name?")

print("Type 'done' when you've added all tasks")
user_word = ""
while user_word.lower() != "done": 
    user_word = input(f"What tasks do you want for {pet}")

    if user_word.lower() == "done":
        break

    tasks.append(user_word)
    print(tasks)