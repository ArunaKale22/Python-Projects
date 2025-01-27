'''
1 for snake
0 for gun
-1 for water 
'''
import random
computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice: ")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

if youStr not in youDict:
    print("Invalid input! Please enter 's' for Snake, 'w' for Water, or 'g' for Gun.")
    exit()
you = youDict[youStr]

print (f"You chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")

if (computer == you):
    print("Its a draw")

else:
    '''
        if(computer == -1 and you == 1): (computer - you) = -2
            print("You win!")

        elif(computer == -1 and you == 0): (computer - you) = -1
            print("You lose!")

        elif(computer == 1 and you == -1): (computer - you) = 2
            print("You lose!")

        elif(computer == 1 and you == 0): (computer - you) = 1
            print("You win!")

        elif(computer == 0 and you == -1): (computer - you) = 1
            print("You win!")

        elif(computer == 0 and you == 1): (computer - you) = -1
            print("You lose!")

            The below logic written on the basis of the value of computer - you.
    '''

    if ((computer - you) == -1 or (computer - you) == 2):
        print("You loose")
    else:
        print ("You win")