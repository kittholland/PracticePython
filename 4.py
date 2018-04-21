number = int(input("Enter a number: "))
print([divisor for divisor in range(1, number) if number % divisor == 0])