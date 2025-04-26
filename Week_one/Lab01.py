# 1. Name: 
#    Tess Hollinger
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    I am making a number guessing game in python 
# 4. What was the hardest part? Be as specific as possible.
#    The Hardest part of this project was trying to set up and film the video! I have never done this before so I strugled to find a way to make a video edditing my screen recording and adding my picture to the frame.
# 5. How long did it take for you to complete the assignment?
#    It took be 30 min to program this, and it took me another 30 min to set up my video app and make the video. So in total I spent 1 hour doing this assignment.   

import random
print("This is the 'guess a number' game.") 

print("You try to guess a random number in the smallest number of attempts.") 
top_int = int(input("Pick a positive integer to set as the max number in the guessing game:  "))

value_random = random.randint(1, top_int)
responses = []
num_of_guesses = 0 
guess = 0; 

while value_random != guess: 
    guess = int(input(f"Guess a number between 1 and {top_int}. "))
    responses.append(guess)
    num_of_guesses += 1 

    if guess > value_random: 
        print("To High!") 
    elif guess < value_random: 
        print("To Low!")
    else: 
        print("You got it!")
         
    
print(f"You were able to find the number in {num_of_guesses} guesses")
print(f"The numbers you guessed were: {responses}")
