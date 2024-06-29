def fibonacci(n):
    fibSeries = [0, 1]
    for i in range(2, n):
        nextFib = fibSeries[-1] + fibSeries[-2]
        fibSeries.append(nextFib)
    return fibSeries

n = int(input("Enter the no. of terms of Fibonacci series: "))
print(fibonacci(n))