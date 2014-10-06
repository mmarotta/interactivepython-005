import simplegui
import random
import math

# int that the player just guessed
player_guess = 0
# the number that the player is trying to guess
secret_number = 0
# the maximum number in the guessing range (default 100)
max_range = 100
# the number of attempt remaining (default 7)
attempts_remaining = 7

# helper function to start and restart the game
def new_game():
    # what range are we working with (0 to 100 by default)
    global max_range, attempts_remaining
    
    # set a random number that the player will try and guess
    global secret_number, max_range
    secret_number = random.randrange(0, max_range)

    # set the number of attempt the player has remaining
    attempts_remaining = int(math.ceil(math.log(max_range, 2)))
    
    # print a welcome message
    print ""
    print "Let's play guess the number, 0 to", max_range
    print "You have", attempts_remaining, "attempts remaining"
    

# define event handlers for control panel
def change_range(new_max_range):
    global max_range, attempts_remaining

    # check the value that was passed in
    max_range = int(new_max_range)
    print "You changed the range to 0 to", max_range
    if (max_range == None):
        max_range = 100

    # start a new game
    new_game()

def input_guess(guess):
    # define the globals
    global secret_number, attempts_remaining

    # print out the player's guess
    print "Guess was", guess
    player_guess = int(guess)

    # decrement guess counter 
    attempts_remaining -= 1
    
    # how did the player do?    
    if player_guess == secret_number:
        print "player wins"
        # let's play again... how about a nice game of chess
        print "That was fun, let's do it again!"
        new_game()
        return
    elif player_guess > secret_number:
        print "too high... ", attempts_remaining, "attempts left"
    elif player_guess < secret_number:
        print "too low...", attempts_remaining, "attempts left"
    else:
        # this should never happen....
        print "i've got a bad feeling about this"

    # check if any attempts left
    if attempts_remaining == 0:
        print "Sorry, you are out of guesses!"
        print "Play again"
        new_game()
        
# create frame
main_frame = simplegui.create_frame('Guess the number', 300, 200)

# register event handlers for control elements and start frame
main_frame.add_input("My Guess is:", input_guess, 100)
main_frame.add_input("Change Range, 0 to:", change_range, 100)
main_frame.start()

# call new_game 
new_game()

