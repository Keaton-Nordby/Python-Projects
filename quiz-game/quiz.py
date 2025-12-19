# we will limit this to 5 questions
# after each quesitons we let user know correct or incorrect
# at the end we compute their score
# questions dict question : anwser


questions = {
    "2 + 2 = ": 4,
    "5 * 3 = ": 15,
    "10 - 6 = ": 4,
    "12 / 4 = ": 3,
    "7 + 8 = ": 15
}


def startGame():
    print("** MATH GAME **")
    choice = input(str("Do you want to play?\n(Yes/No): "))
    if choice.lower() == "no":
        print("Okay, maybe next time!")
        print("END GAME")
    elif choice.lower() == "yes":
        print("**************************")
        print("!! WELCOME TO GAME MODE !!")
        game()
    else:
        print("Invalid option")


def game():

    score = 0
    
    for q, a in questions.items():
        print(q)
        answer = input("Enter your answer as integer: ")
        if int(answer) == a:
            print("CORRECT")
            score += 1
        elif int(answer) != a:
            print("INCORRECT")
        else:
            print("Invalid choice")


    print("*******************")
    print("****GAME OVER****")
    print(f"Your score was {score}/5")


startGame()




        

   
        

    
