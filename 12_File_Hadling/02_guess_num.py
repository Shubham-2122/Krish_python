import random

num = random.randint(1,20)


while True:
    guess = int(input("Enter your Number between 1 to 20 : "))
    if guess == num:
        print("You guessed A correct Number")
        break
    elif guess>num:
        print("You guessed a grather Number")
    elif guess<num:
        print("you Guessed a Smaller Number")
