import random

def passwordGenerator(n):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`!@#$%^&*_"
    if n > len(characters):
        chosen_letters = random.choices(characters, k = n)
    else:
        chosen_letters = random.sample(characters, n)
    password = ''.join(chosen_letters)
    return password

n = int(input("Enter the length of password: "))
result = passwordGenerator(n)
print("Your password is:", result)