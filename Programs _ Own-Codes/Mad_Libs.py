def welcome():
    print("Welcome to the game of MadLibs!!")
    print("Enter the directed type of words below, when asked")
def madlibs_gen():
    person_name = input("Enter your name: ")
    person_name2 = input("Enter name of a person: ")
    person_name3 = input("Enter one more name of a person: ")
    person_name4 = input("Enter a last name of a person: ")
    num = input("Enter a number from 1-100: ")
    adjective = input("Enter an adjective: ")
    color = input("Enter a colour: ")
    noun = input("Enter a noun(Monument): ")
    noun2 = input("Enter a noun(Vehicle): ")
    food_type = input("Enter a type of food (Plural): ")
    verb_ing = input("Enter a verb ending in 'ing': ")
    clothing = input("Enter an article of clothing: ")
    celeb = input("Enter a name of Celebrity: ")
    num2 =  input("Enter a number from 1-365: ")
    occupation = input("Enter an occupation: ")
    print("\n\n")

    print("The final story comes out as:\n")
    print(f"My name is {person_name} and I am {num} years old. If I were president, I'd \n"
          f"do a whole bunch of {adjective} things:-\n"
          f"1. I would drive the biggest {color} car in the country. And that car\n"
          f"would go faster than any other {noun2} in the world!\n\n"
          f"2. Everyone would eat pepperoni {food_type} for dinner.\n\n"
          f"3. I would live in the statue of {noun} and build a {verb_ing} pool at her feet.\n\n"
          f"4. I would wear a {clothing} on my head, and everyone would say I look \n"
          f"{adjective} like {celeb}.\n\n"
          f"5. School would be open only {num2} days a year.\n\n"
          f"6. I would give my friends the best jobs, I would nominate {person_name2} to be secretary of (the)\n"
          f"{person_name3} and {person_name4} could be vice {occupation}.\n\n")


welcome()
madlibs_gen()
