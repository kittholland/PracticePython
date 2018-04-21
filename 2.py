number = int(input("Enter a number: "))
checkNum = int(input("Enter a divisor: "))
if number % checkNum == 0:
    print(f"{number} is a multiple of {checkNum}")
else:
    print(f"{number} is not a multiple of {checkNum}")