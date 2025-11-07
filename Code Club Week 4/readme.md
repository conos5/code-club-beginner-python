# Code Club Week 4    
  
## Start  
- Use **mist** platform for Red-Hat Wi-Fi  
- Check if there are any new kids joining - will need to give extra time to recap if there is or have someone with them a lot of time to make sure they can follow class.  
  
## Recap  
- Recall taking ***input***  
    - Key parts to remember is that the parameter to the input function should be the prompt or question for what you want to get from user!  
        - Many kids were putting the answer itself in the param section: **number = input("6")** etc.  
```
sides = input("How many sides are on your dice?”)
```
- Storing input in variables ^: make sure *correct type* is used: **type conversion** (eg. **int()**)  
- Have the roll_dice.py program on screen and walk through it focusing on these ideas above (no longer than 3-5 mins unless there is a new kid  
  
## Conditionals  
### Real-World Examples Discussion (3 minutes)  
Ask students: "When do we make decisions in real life?"  
- If it's raining → take umbrella  
- If it's hot → wear shorts  
- If you're hungry → eat food  
  
### Why We Need Conditionals in Code (2 minutes)  
"Computers need to make decisions too! Games like rock-paper-scissors, checking passwords, or deciding if someone wins or loses."  
  
### Start with ***if condition***  
- **if** keyword starts the condition  
- Similar to writing a function:  
    - Colon ‘**:**’ ends the condition line  
    - Indentation matters! (Tab) everything tabbed below if is *inside* it, only happens if the condition is met  
- Code after the if block always runs  
  
Show **temperature-if.py** file.Simple if statement program.  
Show how while this is useful, oftentimes we want to control what happens when the condition is not true also  
  
### Else condition  
The else condition literally happens as ***what happens if this condition is not met / true***  
  
Example: **temperature-else.py**  
  
We can now handle both sides.  
  
### Example Program: Coin Flip Game  
- We will make a simple coin-flip game using **if-else** and what we learned last week about ***taking input*** and using ***random.randint***  
- To teach this, don’t just show **coin-flip.py**, rather write out starting from the things they know:  
    - Import random (they have done but easy to forget)  
    - Taking input: they know how to. Prompt them that we want an input of 0 or 1, 0=heads, 1=tails  
    - They know how to use random.randint  
        - Then we tell them that this time instead of a range of 1,6 (like a dice), we will set it to 0,1  
    - Then the new stuff comes in with the conditionals  
    - Very simple:  
        - If players choice = coin:  
            - Player wins  
        - Else (if they are not equal):  
            - Player loses  
```
Write this out on the white board in words or pseudo code style so they can follow
```
- When then writing this out in program, explain why we use ‘**==**‘ instead of just ‘**=**‘  
    - Because this way the program doesn’t get confused with ‘=‘ which is for setting a variable as we have seen.  
    - ‘**=**‘: setting a variable  
    - ‘**==**‘ check if 1st equals the 2nd  
  
### Elif Condition  
What if we want to have another condition!  
- To do this, in python we do an ‘**elif**’: “*else if*"  
- Important that order matters  
    - Top to bottom  
    - If first, then elif(s), then else  
    - Generally it is:  
        - 1 if  
        - Many elif’s  
        - 1 else  
- Example program: **guess-number-if.py**  
- This program uses if’s, elif’s, and else’s for guessing a secret random number  
    - Make sure to explain the operators of ‘>’ and ‘<‘: like in maths  
    - Note that the else here handles the final case that we have not accounted for (in this example, “Too high”)  
```
What is a limitation of this program?
Would be nice to be able to keep trying to guess the number after it tells too high / too low ?
This is something we will look at next week
```
