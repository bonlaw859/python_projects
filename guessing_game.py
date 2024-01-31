# imported libraries

import random

# Constants

MAX = 100

# The main program
# ----------------

def main():
    introduction()

    #create initial total attempts list
    
    total_attempts = []

    # A sentinel loop to keep playing after each game is done

    continue_playing = True
    
    while continue_playing:
        total_attempts = play_a_game(total_attempts)
        play_again = input('Do you want to play again? ')

        #stop playing if user answers anything that doesnt start with a y
        
        if play_again.lower()[0] != 'y':
            continue_playing = False
    
    statistics(total_attempts)

# Supporting functions (in alphabetical order)
# --------------------------------------------

# a function that prints an intro haiku

def introduction():
    print("Guess any number")
    print("A digit of my choosing")
    print("It's probably fun.")
    print()

# A function that plays one game

def play_a_game(total_attempts):

    #set variables to start
    
    correct_val = random.randint(1, MAX)
    user_guess = 0
    attempts = 0

    print(f'I\'m thinking of a number between 1 and {MAX}... ')

    #check if guess is correct and respond accordingly, updating attempts

    while user_guess != correct_val:
        user_guess = int(input('Your guess? '))

        if user_guess < correct_val:              
            print('It\'s higher.')
            attempts += 1

        elif user_guess > correct_val:
            print('It\'s lower.')
            attempts += 1

        else:
            attempts += 1
            print(f'You got it right in {attempts} guesses!')

    #append list and return

    total_attempts.append(attempts)
    
    return total_attempts

# a function that displays the statistics

def statistics(total_attempts):

    #calculate stats
    
    total_games = len(total_attempts)
    total_guesses = sum(total_attempts)
    average_guesses = total_guesses / total_games
    best_game = min(total_attempts)

    #print stats

    print('Overall results:')
    print(f'Total games = {total_games}')
    print(f'Total guesses = {total_guesses}')
    print(f'Guesses/ game = {average_guesses}')
    print(f'Best game = {best_game}')

#call main

main()
