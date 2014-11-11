
#Kamariddinkhon Fazliddin
#Desert Escape.
#This game is a turn based game.
#The objective of the game is to escape the natives with the camel safely.
#Camel cannot die from starvation or tiredness.
#Once the player travels over 200 miles, the game is won.



import random

miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_traveled = -20
number_drinks_canteen = 3


print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")

done = False
letter = ""
while done is False:
    print()
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    
    
    letter = input("Please enter your choice: ").upper()
    print()
    oasis = random.randrange(1, 20)
    if oasis == 1:
        print("You found Oasis")
        number_drinks_canteen = 3
        thirst = 0
        camel_tiredness = 0
    
    
    
    if letter == "Q":
        done = True
        print("quit")
        break

    elif letter == "E":
        print("Miles traveled:", miles_traveled )
        print("Drinks in canteen:", number_drinks_canteen)
        print("The natives are", miles_traveled - natives_traveled ,"miles behind you.")


    elif letter == "D":
        print("The camel is happy")
        camel_tiredness = 0
        natives_traveled += random.randrange(7 , 14)
            
    elif letter == "C":

        thirst += 1
        camel_tiredness += random.randrange(1, 3)
        miles_traveled += random.randrange(10, 20)
        natives_traveled += random.randrange(7 , 14)
        print("you have traviled", miles_traveled, "miles")
    elif letter == "B":
        miles_traveled += random.randrange(5, 12)
        print("you have traviled", miles_traveled, "miles")
        thirst += 1
        camel_tiredness += random.randrange(1, 3)
        natives_traveled += random.randrange(7 , 14)
    elif letter == "A":
        if number_drinks_canteen > 0:
            thirst = 0
            number_drinks_canteen -= 1
        else:
            print("No more drinks")
    if thirst > 4:
        print("You are thirsty")
    if thirst > 6:
        print("You died of thirst")
        done = True
        break
    if camel_tiredness > 5:
        print("Your camel is getting tired")
    if camel_tiredness > 8:
        print("Your camel is dead")
        done = True
        break
    if miles_traveled <= natives_traveled:
        print("You got caught")
        done = True
        break
    elif (miles_traveled - natives_traveled) < 15:
        print("The natives are getting close!")
    if miles_traveled > 200:
        print("You won the game")
        done = True
        break
    

