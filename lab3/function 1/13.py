import random

print("Hello! What is your name?")
name = input()

print("\nWell,", name, ",I am thinking of a number between 1 and 20.\nTake a guess.")

ranum = random.randrange(1,20)
n = 0   #num of guesses

while(True):
    n += 1   #increment num of guesses
    a = int(input())
    print()
    if(a == ranum): #correct guess
        print("Good job,",name,"! You guessed my number in",n, "guesses!")
        break
    elif(a > ranum): #guess is too high, informs the player 
        print("Your guess is too high.\nTake a guess.")
    else:            #guess is too low, informs the player
        print("Your guess is too low.\nTake a guess.")        