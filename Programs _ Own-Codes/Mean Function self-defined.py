def mean(*numbers):
    return sum(numbers) / len(numbers)

i = int(input("1st Num: "))
j = int(input("2nd Num: "))

print(mean(i, j))