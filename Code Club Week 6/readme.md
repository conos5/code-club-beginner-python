# Code Club Week 5

## Start
- Use mist platform for Red-Hat Wi-Fi (https://pskportal.mist.com/#!byod/6c5e0fc3-3a1f-4bdd-998d-1e0c6af1af66?exp=1759050834.5621297&jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IkNvbm9yLlNoaXBzZXlAaWJtLmNvbSIsImV4cCI6MTc1OTA1MDgzNC41NjQzNDc3LCJwc2twb3J0YWxfaWQiOiI2YzVlMGZjMy0zYTFmLTRiZGQtOTk4ZC0xZTBjNmFmMWFmNjYiLCJ0eXBlIjoiYnlvZCIsImlkIjoiRklNUlNQXzhhNzM0MzQ3LTAxOTktMTUxNS1hYWRkLWY4MmMyM2QzMjBiYSIsInJvbGUiOiJJQk0ifQ.xlvHxrvkzRpe6BETnsYE76USd2SQh4K9aCQtRZbhOFU)
- Boot up local environment (https://editor.raspberrypi.org/en/projects/blank-python-starter or VSCode)
- Check for new students

## PART 1: Recap & Practice Exercises (30-45 minutes)

### Introduction (2 minutes)
"Last week we learned while loops - one of the most powerful tools in programming! Today we'll practice more with different examples, then learn about lists which let us store multiple things in one variable."

### Quick Recap: The 3 Parts of a While Loop (5 minutes)

Write on whiteboard:
1. DECLARE variable (starting value)
2. SET CONDITION (when to keep looping)
3. UPDATE variable (so it eventually stops)

- Give example code of like a count to five program

### Exercise 1: Countdown Timer (6 minutes)

**Combines:** while loops, input, variables, conditionals

##### Teaching points:

- Variable can *decrease* instead of increase
- Condition checks when to stop
- Shows practical use of while loops (like a rocket countdown!)

### Exercise 2: Password Checker (4 minutes)

- Pretty much already covered
- Reminder that we can use words to compare for a loop
- This time the update will be by getting input each time
- We can also track other variables like attempts
- Remember `!=`("not equals") and `==`("equals") are the way to compare

- Added check for attempts
    - Introduces idea of logical `and`

### Exercise 3: Advanced Calculator (10-20 minutes)

- User controls loop limit
- Conditional BEFORE loop to validate input
- Two variables updating: count and total
- Shows off f-string with expressions

- This one will be a challenge with syntax, indentation especially

#### Now add lists in to it:
"What if we wanted to store all the numbers entered, not just the total? We'd need a way to store multiple values..." → Perfect segue to lists!

- Show before break if can, then explain after

## Part 2: Intro to Lists

### The Problem with Single Variables (3 minutes)

"Lets say you want to store your 5 favourite foods, how would we do it"

- Square brackets [] create a list
- Items separated by commas
- Lists can hold strings, numbers, or mix!
- You can pick items out of a list with an *Index*
    - Indexes start with 0, instead of 1

"A list is like a row of boxes. In this case there are infinite boxes and we can store anything in each box. Each box is labelled with a number that we can then open it with"

### Exercise 1: Random food picker

"Let's use this indexing for something using our random number generator"

There are lots of different things we can do with lists:
- Eg. using the `random.choice` method
- `append`
- `len`
- `pop`

`random-food-picker.py`

### Exercise 2: Shopping list

- Empty list: `[]`
- `.append()` adds to end of list
- `len()` gets list length
- First introduction to for loop for printing (preview for next week)
- While loop controls when to stop adding

`shopping-list.py`

### Very common issues

- Use square brackets
- Index must start at 0
- Index out of range errors
- Trying to access empty list



### Link to Dropbox with Previous Classes:

https://www.dropbox.com/scl/fo/gr5buf7pewc6gjysul66u/APup7GPWHlovgsWFflHX1Fw?rlkey=ic9r4xvhfnwi11qg8uhmd9ld3&st=ewvv9oge&dl=0