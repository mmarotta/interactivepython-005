# implementation of card game - Memory

import simplegui
import random

NUM_CARDS = 16
exposed = [False] * NUM_CARDS

# create the list of cards
cards = []
cards.extend(range(0, NUM_CARDS/2 + 1))
cards.extend(range(0, NUM_CARDS/2 + 1))

# cover all cards
def cover_all_cards():
    global exposed
    exposed = [False] * NUM_CARDS

# helper function to initialize globals
def new_game():
    # shuffle the deck
    random.shuffle(cards)
    
    # cover all the cards
    cover_all_cards()
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    # draw the cards on the canvas
    x = 0
    for card in cards:
        canvas.draw_text(str(card), [x, 70], 60, 'White', 'monospace')
        x += 50
        
    # cover the unseen cards
    x = 0
    for is_seen in exposed:
        if not is_seen:
            canvas.draw_polygon([[x+2,2], [x+48,2], [x+48,98], [x+2,98]], 1, 'Green', 'Green')
        x += 50
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
