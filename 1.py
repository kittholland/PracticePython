name = input("Enter your Name:")
age = int(input("Enter your Age:"))
yearsTo100 = str((100-age)+2018)
print(f"Your name is {name} and you are {age} years old.")
ageMessage = "You will be 100 in " + yearsTo100
print(ageMessage)
multiplier = int(input("How many times would you like to see that dumb message?"))
newLineAgeMessage = ageMessage + "\n"
print(f"{newLineAgeMessage*multiplier}")