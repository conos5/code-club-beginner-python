# The Never-Ending Copycat
print("I will copy everything you say. Type 'stop' to end.")

user_word = ""

# Keep looping while the word is NOT 'stop'
while user_word != "stop":
    user_word = input("Say something: ")
    
    if user_word != "stop":
        print("Copycat says: " + user_word)

print("Okay, I'll stop now.")
