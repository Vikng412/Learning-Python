import time

ptime = time.strftime("%H:%M")
qtime = int(time.strftime("%H"))

if qtime < 12:
    print("It's " + ptime + " AM" + "\nGood morning Sir")
elif 12 < qtime < 18:
    print("It's " + ptime + " PM" + "\nGood afternoon Sir")
elif 18 < qtime < 21:
    print("It's " + ptime + " PM" + "\nGood evening Sir")
elif qtime > 21:
    print("It's " + ptime + " PM" + "\nGood night Sir")
