# Factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


i = int(input("Put the number, to find its factorial: "))
print(factorial(i))


# Fibonacci Sequence
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


j = int(input("Put a number to find its Fibonacci sequence: "))

print(fibonacci(j))
