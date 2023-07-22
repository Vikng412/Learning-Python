def is_leap(year):
    if int(year % 4) == 0:
        if int(year % 100) == 0:
            if int(year % 400) == 0:
                leap = True
            else:
                leap = False
        else:
            leap = False
    else:
        leap = False
    return leap


year = int(input())
# print(is_leap(year))

if 1900 <= year <= 100000:
    print(is_leap(year))
else:
    print("Invalid Input!!")
    quit()
