from random import randint
guess = None
number = str(randint(1000, 9999))
while guess != number:
    guess = input("Please enter a 4 digit number: ")
    cows = 0
    bulls = 0
    if guess == number:
        print("You Win!")
        break
    for i in range(0,3):
        if number[i] == guess[i]:
            cows += 1
        elif guess[i] in number:
            bulls += 1
    print(f"{cows} Cows, {bulls} Bulls.")