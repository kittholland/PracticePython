number = int(input("Enter the number of fibonacci numbers you would like: "))

def fibonacci(number):
    if number < 3:
        return(1)
    return fibonacci(number-1) + fibonacci(number-2)

print([fibonacci(n) for n in range(1,number)])