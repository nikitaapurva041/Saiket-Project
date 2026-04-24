# import random 
import random
# variable for storing the random number
cnumber=random.randrange(1,100)
usernumber=int(input("Enter a number between 1 and 100: "))
# attempts for the user to guess the number
attempts= 0 
# loop for checking the user input with the random number
while True:
# loop for checking the user input with the random number
    attempts +=1
    if cnumber > usernumber:
        print("The computer number is", cnumber)
        print("Your number is smaller than the computer number")
       
    elif cnumber < usernumber:
        print("The computer number is", cnumber)
        print("Your number is greater than the computer number")
    else:
        print("The computer number is", cnumber)
        print("You guessed the number correctly")
    print("You took", attempts, "attempts to guess the number")
    
    break
