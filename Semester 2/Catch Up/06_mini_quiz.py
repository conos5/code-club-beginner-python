# === LESSON 6: MINI QUIZ ===
# Let's put it all together! This uses everything from lessons 1-5.

# Step 1: Set up the score and questions
score = 0
questions = ["What planet do we live on?", "What colour is grass?", "How many legs does a spider have?"]
answers = ["earth", "green", "8"]

# Step 2: Loop through each question
for i in range(len(questions)):
    print(f"\nQuestion {i + 1}: {questions[i]}")
    guess = input("Your answer: ").lower()

    # Step 3: Check the answer
    if guess == answers[i]:
        print("Correct!")
        score = score + 1
    else:
        print(f"Nope! The answer was: {answers[i]}")

# Step 4: Show final score
print(f"\nYou got {score} out of {len(questions)}!")

if score == len(questions):
    print("Perfect score!")
elif score >= 2:
    print("Nice work!")
else:
    print("Better luck next time!")


# === YOUR TURN ===
# 1. Change the questions and answers to your own
# 2. Add more questions (make sure to add an answer for each one!)
# 3. Can you add a question that uses a number answer?
#    Hint: you'll need to keep the answer as text in the list — "8" not 8
