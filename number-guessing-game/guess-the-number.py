# user should be let known of range of numbers
# count will count how many times a user took to guess the number
# will show if they got it correct
# will also give hints (higher or lower)
import random


def game():

    answer = random.randint(0, 15)
    guesses_count = 0
    print("****NUMBER GUESSING GAME****")
    game_in_progress = True
    
    while game_in_progress:
        guesses_count += 1
        guess = input("Guess a number between 0-15: ")
        if int(guess) == answer:
            print(f"You guessed correct! It took you {guesses_count} tries.")
            game_in_progress = False
            break   
        elif int(guess) > answer:
            print("Sorry you guessed too high, try again.")
            
        elif int(guess) < answer:
            print("Sorry you guessed too low, try again.")
            
        else:
            print("Invalid choice")

    print("****GAME OVER****")

game()



    
