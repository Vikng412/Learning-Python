from typing import List

# Questions

q1 = "Q1.\nWhat is the capital of India? (Reward: ₹10,000)"
q2 = "Q2.\nWhat is the capital of U.P?  (Reward: ₹1,00,000)"
q3 = "Q3.\nName the currency of India. (Reward: ₹10,00,000)"
q4 = "Q4.\nWho is the current P.M.? (Reward: ₹1,00,00,000)"
q5 = "Q5.\nWho is the current President of India? (Reward: ₹7,00,00,000)"

# a1 = "Delhi"
# a2 = "Bhopal"
# a3 = "Rupee"
# a4 = "Narendra Modi"
# a5 = "Draupadi Murmu"

# Options

o1 = ["A: Mumbai", "B: Hyderabad", "C: Delhi", "D: Bangalore"]
o2 = ["A: Prayagraj", "B: Bhopal", "C: Lucknow", "D: Amethi"]
o3 = ["A: Rupee", "B: Dollar", "C: Dhiram", "D: Peso"]
o4 = ["A: Dr. Manmohan Singh", "B: Rahul Gandhi", "C: Rajiv Gandhi", "D: Narendra Modi"]
o5 = ["A: Pranab Mukherji", "B: Ramnath Kovind", "C: Draupadi Murmi", "D: Rahul Gandhi"]

# About Contestant

name = input("What is your Name?: ")
print("Hi, " + name)

confirm = input("Are you ready??: ")
if confirm == "Y" or "Yes" or "y" or "yes":
    print("Ok then Let's Start\n")
elif confirm == "N" or "No" or "n" or "no":
    print("Ok take your time")
else:
    print("Invalid Input")

# List of Questions & Options

questions = [q1, q2, q3, q4, q5]
options = [o1, o2, o3, o4, o5]

# Actual Questioning & Answering

# Question 1
print(questions[0])
print(options[0])

a1 = input("\nWhat's Your Answer? (A/B/C/D): ")

if a1 == "C" or "c":
    print("\nSahi Jawaab, 10 Hazaar!!\n")
else:
    print("\nAfsos, Galat Jawab.")
    print("\nAap yahan se ghar le jaayenge, 10,000 rupaye ki dhanrashi")
    exit()

# Question 2

print(questions[1])
print(options[1])

a2 = input("\nWhat's Your Answer? (A/B/C/D): ")

if a2 == "B" or "b":
    print("\nSahi Jawaab, 1 lakh!!\n")
else:
    print("\nAfsos, Galat Jawab.")
    print("\nDurbhagyawash aap yahan se koi dhanrashi nahi jeet ke jaayenge ")
    exit()

# Question 3

print(questions[2])
print(options[2])

a3 = input("\nWhat's Your Answer? (A/B/C/D): ")

if a3 == "A" or "a":
    print("\nSahi Jawaab, 10 lakh!!\n")
else:
    print("\nYe Galat Jawab hai.")
    print("\nAap yahan se ghar le jaayenge, 1,00,000 rupaye ki dhanrashi")
    exit()

# Question 4

print(questions[3])
print(options[3])

a4 = input("\nWhat's Your Answer? (A/B/C/D): ")

if a4 == "D" or "d":
    print("\nBohot Khoob, 1 Crore!!\n")
else:
    print("\nOho, Galat Jawab, aap gir ke aagaye hain doosre padaw pe")
    print("\nAap yahan se ghar le jaayenge, 1 Lakh rupaye ki dhanrashi")
    exit()

# Question 5

print(questions[4])
print(options[4])

a5 = input("\nWhat's Your Answer? (A/B/C/D): ")

if a5 == "C" or "c":
    print("\n7 CRORE!!!")
    print("\nAap yahan se ghar le jaayenge, 7 Crore rupaye ki dhanrashi \nBadhaayi ho!!")
else:
    print("\nAfsos, Galat Jawab, aap gir ke aagaye hain doosre padaw pe")
    print("\nAap yahan se ghar le jaayenge, 1 Lakh rupaye ki dhanrashi")
    exit()

