import random

def rock_paper_scissor():
    choices = ["rock", "paper", "scissor"]

    while True:
            user_Choice = input("Enter rock, paper or scissor(or 'q' to quit): ")

            if user_Choice == "q":
                break
            if user_Choice not in choices:
                print("Enter a valid choices, amongst rock, paper or scissor")
                continue

            computer_choice = random.choice(choices)

            print(f"Computer chooses {computer_choice}.")

            if user_Choice == computer_choice:
                print("It's a tie!")
            elif (user_Choice == "rock" and computer_choice == "scissor" ) or (user_Choice == "paper" and computer_choice == "rock") or (user_Choice == "scissor" and computer_choice =="paper"):
                print("You Win!")
            else:
                print("Computer Wins!")

rock_paper_scissor()
