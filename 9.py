import random
number = random.randint(1, 9)
won = False
guessCount = 0
while True:
    guess = input("Guess a number between 1 and 9 - or type exit to quit: ")
    if guess == "exit":
        break
    else:
        guess = int(guess)
    guessCount += 1
    if number > guess:
        print("Higher...")
    elif number < guess:
        print("Lower...")
    else:
        print(f"You got it in {guessCount} guesses!")
        break