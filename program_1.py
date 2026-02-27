
import random

# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.

def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    # Sum 2 numbers
    total = die1 + die2
    # return sum to calling function
    return total

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop. 
total_sum = 0
for i in range(100):
    total_sum += randDice()
average = total_sum / 100
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
print(f"Average of 100 rolls: {average:.2f}")

