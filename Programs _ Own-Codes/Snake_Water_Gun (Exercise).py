import random

def snake_water_gun():
    choices = ["snake", "water", "gun"]

    while True:
            user_Choice = input("Enter snake, water or gun(or 'q' to quit): ")

            if user_Choice == "q":
                break
            if user_Choice not in choices:
                print("Enter a valid choices, amongst snake, water or gun")
                continue

            computer_choice = random.choice(choices)

            print(f"Computer chooses {computer_choice}.")

            if user_Choice == computer_choice:
                print("It's a tie!")
            elif (user_Choice == "snake" and computer_choice == "water" ) or (user_Choice == "gun" and computer_choice == "snake") or (user_Choice == "water" and computer_choice =="gun"):
                print("You Win!")
            else:
                print("Computer Wins!")

snake_water_gun()

