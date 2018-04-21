won = False
while won == False:
    playerOne = input("Player One: please input Rock, Paper, or Scissors: ").lower()
    playerTwo = input("Player Two: please input Rock, Paper, or Scissors: ").lower()
    if playerOne == "rock":
        if playerTwo == "scissors":
            winner = "Player One"
            won = True
        elif playerTwo == "paper":
            winner = "Player Two"
            won = True
    if playerOne == "scissors":
        if playerTwo == "rock":
            winner = "Player Two"
            won = True
        elif playerTwo == "paper":
            winner = "Player One"
            won = True
    if playerOne == "paper":
        if playerTwo == "rock":
            winner = "Player One"
            won = True
        elif playerTwo == "scissors":
            winner = "Player Two"
            won = True
    if winner:
        print(f"{winner} Wins!")