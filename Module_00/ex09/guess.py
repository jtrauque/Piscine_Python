import random

print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n")
fix = random.randint(1, 99)
num = 0;

while True:
    inp = input("What's your guess between 1 and 99?\n>> ")
    num += 1
    if inp.isdigit() and int(inp) > 1 and int(inp) < 99:
        guess = int(inp)
        if guess < fix:
            print("Too low!")
        elif guess > fix:
            print("Too high!")
        else:
            print("Congratulations, you've got it!\nYou won in %d attempts!\n" %(num))
            break 
    elif inp.isdigit():
        print("The number has to be between 1 and 99")
    elif inp == 'exit':
        print("Thank you for playing with us and see you soon!")
        break
    else:
         print("That's not a number.")
