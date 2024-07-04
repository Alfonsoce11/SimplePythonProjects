import random
print("Guess a number between -100 and 100. You have 5 guesses.")
theNumber = random.randint(-100, 100)
userGuess = int(input("Make your guess: "))
if userGuess == theNumber:
    print("You guessed right!")
elif userGuess > theNumber:
    print("Your guess was too high")
elif userGuess < theNumber:
    print("Your guess was too low")

if userGuess != theNumber:
    print("Try again")
    userGuess2 = int(input("Make your second guess: "))
    if userGuess2 == theNumber:
        print("You guessed right!")
    elif userGuess2 > theNumber:
        print("Your guess was too high")
    elif userGuess2 < theNumber:
        print("Your guess was too low")

if userGuess2 != theNumber:
    print("Try again")
    userGuess3 = int(input("Make your third guess: "))
    if userGuess3 == theNumber:
        print("You guessed right!")
    elif userGuess3 > theNumber:
        print("Your guess was too high")
    elif userGuess3 < theNumber:
        print("Your guess was too low")

if userGuess3 != theNumber:
    print("Try again")
    userGuess4 = int(input("Make your fourth guess: "))
    if userGuess4 == theNumber:
        print("You guessed right!")
    elif userGuess4 > theNumber:
        print("Your guess was too high")
    elif userGuess4 < theNumber:
        print("Your guess was too low")

if userGuess4 != theNumber:
    print("Try again")
    userGuess5 = int(input("Make your fifth and last guess: "))
    if userGuess5 == theNumber:
        print("You guessed right!")
    elif userGuess5 > theNumber:
        print("Your guess was too high. The number was ", theNumber)
    elif userGuess5 < theNumber:
        print("Your guess was too low. The number was ", theNumber)
