# Code Club Week 5

## Start
- Use mist platform for Red-Hat Wi-Fi
- Boot up local environment (https://editor.raspberrypi.org/en/projects/blank-python-starter or VSCode)
- Check for new students - assign a mentor for one-on-one support if needed
- Total time: ~90 minutes (split into two sections)

## PART 1: Recap & Practice Exercises (30-45 minutes)

### Introduction (2 minutes)
“Today we’ll practice everything we’ve learned: variables, input, functions, f-strings, and conditionals. Then we’ll learn something new that makes our programs way more powerful!”

### Exercise 1: Mad Libs Game (8-10 minutes)
Combines: variables, input, f-strings

Teaching points:
- Multiple variables from input
- F-strings with multiple variables
- Using `\n` for new lines

`mad-libs.py`


### Exercise 2: Simple Calculator (10-12 minutes)
Combines: input, type conversion, conditionals, operators

`simple-calculator.py`


## PART 2: Introduction to While Loops (40-45 minutes)
### The Problem (3 minutes)
Show the original `guess-number.py` from last week

- This uses if, elif, and else conditionals

Ask students: “What’s the problem with this game?”
	•	Only get one guess!
	•	Would be more fun to keep guessing until we get it right

### Introducing While Loops (5 minutes)

**Explanation:**
“A `while` loop keeps repeating code as long as a condition is true. Like saying ‘while I’m hungry, keep eating.’”

Simple example to write on whiteboard:
```
while (condition is true)
    do something
    do something else
```

#### Count to five
On whiteboard:
- So how could we use a while loop to count to five?

`count-to-five.py`

###### Teaching points:
- While loop structure similar to `if` (colon, indentation)
- Condition checked before each repetition
- Must change something inside loop or it runs forever!
- `count = count + 1` increments the variable

### Number Guessing Game with While
Now we will make a simple number guessing games
`guess-number-basic-while.py`

- We have a loop which only stops once you guess the number
    - We do a "While guess is not equal to the secret number"
- Therefore this loop keeps asking for your next guess until you get it right

This could be better however with some hints like 'too high' or 'too low'

`guess-number-while.py`

- Now we have added some conditionals to make this program more fun and easy to play!

#### Challenge Extension (Optional, 5 minutes)
If students finish early:

###### Counter for number guesser
- Could we add a counter for the number of tries that it takes for the user to guess the number correctly?

###### Coin Flip with continue playing
- While loop with string condition
- User controls when loop ends
- Making a replayable game

## Wrap-Up

### Key Concepts Review
- While loops repeat code while condition is true
- Must change something inside loop to eventually stop
- Combine loops with conditionals for powerful programs
- Infinite loops = forgot to change the condition
### Questions to Ask:
- “What’s the difference between `if` and `while`?”
    - `if` runs once, `while` keeps repeating
- “When would we use a while loop?”
    -  When we want to keep doing something until a condition changes