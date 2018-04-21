number = int(input("Enter a number: "))
if len([divisor for divisor in range(1, number) if number % divisor == 0]) > 2:
    print(f"{number} is not prime.")
else:
    print(f"{number} is prime.")