questions = [
    ["What is the capital of India?", "Mumbai", "Hyderabad", "Delhi", "Bangalore", 3], #1
    ["What is the capital of U.P?", "Prayagraj", "Bhopal", "Lucknow", "Amethi", 3], #2
    ["Name the currency of India.", "Rupee", "Dollar", "Dhiram", "Peso", 1], #3
    ["Who is the current P.M.?", "Dr. Manmohan Singh", "Rahul Gandhi", "Rajiv Gandhi", "Narendra Modi", 4], #4
    ["Who is the current President of India?", "Pranab Mukherji", "Ramnath Kovind", "Draupadi Murmu", "Rahul Gandhi", 3], #5
    ["Which Great Personality Person is known as “Saint Of The Gutter”?", "Rahul Gandhi", "Indra Gandhi", "Mother Teresa", "Subhash Chandra Bose", 3], #6
    ["Entomology is the science that studies", "Behavior of human beings", "Insects", "The origin and history of technical and scientific terms", "The formation of rocks", 2], #7
    ["For which of the following disciplines is Nobel Prize awarded?", "Physics and Chemistry", "Physiology or Medicine", "Literature, Peace and Economics", "All of the Above", 4], #8
    ["Who is the fastest man of the world?", "Usain Bolt", "Milkha Singh", "James Cameron", "Major Dhyanchand", 1], #9
    ["Which person holds the title of 'The Flying Sikh'?", "Major Dhyanchand", "Manminder Brar", "Rafael Nadal", "Milkha Singh", 4], #10
    ["Hitler party which came into power in 1933 is known as?", "Labour Party", "Nazi Party", "Ku-Klux-Klan", "Democratic Party", 2],#11
    ["What is the full form of 'etc.'?", "Et Cetra", "Ecetra", "Excetra", "Extra", 1],#12
    ["What does 'WHO' stands for?", "World Hair Organisation", "World Help Organisation", "World Health Organisation", "World Hare Organisation", 3],#13
    ["What was the name of the place where the most recent collision of trains occured in India?", "Odisha", "Kolkata", "Balasore", "West Bengal", 3],#14
    ["Who is the author of the book 'Experiments With truth'?", "Jawaharlal Nehru", "Mahatma Gandhi", "S.C. Bose", "Rajendra Prasad", 2],#15
    ["Who is the person who discovered most of the planets?", "Isaac Newton", "Albert Einstein", "Galileo", "Stephen Hawking", 3]#16
]

levels = [0, 1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 70000000]

# Introduction of Contestant
name = input("Hey, What is your Name?: ")
print(f"Namaskar {name}, Chaliye Khel prarambh karte hain.")

# Loop
money = 0
try:
    for i in range(0, len(questions)):

    # Questioning
        question = questions[i]
        print(f"\n------------Ye sawaal, {levels[i+1]} ke liye.------------")
        print(f"\n{question[0]}")
        print(f"1. {question[1]}            2.{question[2]}")
        print(f"3. {question[3]}             4.{question[4]}")
        ans = int(input(f"What's Your Answer? (1-4) (press 0 to quit): "))

    # Answer Checker
        if ans == question[-1]:
            print(f"\nSahi jawaab, aap jitte hain Rs.{levels[i+1]}")
        # Winning Amount
            if i == 4:
                money = 10000
            elif i == 9:
                money = 320000
            elif i == 14:
                money = 10000000
            elif i == 15:
                money = 70000000
                print(f"\n~~~~~{name} Ji, aap yahan se leke jaayenge Rs.{money} ki dhanrashi.~~~~~")
        # Quit Game
        elif ans == 0:
            print(f"\n~~~~~{name} Ji, aapne game quit karne ka faisla liya hai, aap yahan se leke jaayenge Rs.{levels[i]} ki dhanrashi.~~~~~")
            break
        else:
            print("Afsos Galat Jawab!!")
            print(f"\n~~~~~ {name} Ji, aap yahan se leke jaayenge Rs.{money} ki dhanrashi.~~~~~")
            break

except ValueError:
    print("Invalid Input, try again")



