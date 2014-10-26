import simplegui
import random

NUM_CARDS = 16
exposed = []
this_turn = []
total_turns = 0

# create the list of cards
cards = []
cards.extend(range(0, NUM_CARDS/2))
cards.extend(range(0, NUM_CARDS/2))

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
    # reset the turn counter
    turn_change(0)

# define event handlers
def mouseclick(pos):
    # determine which card was clicked
    card_clicked = pos[0] // 50
    # make sure card is not already showing before kicking a change
    if not exposed[card_clicked]:
        state_change(card_clicked)
                        
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

def turn_change(x):
    global total_turns
    if x == 1:
        total_turns += 1
    elif x == 0:
        total_turns = 0
    label.set_text("Turns = " + str(total_turns))
        
def state_change(card_clicked):
    # show the card that was clicked
    exposed[card_clicked] = True
    # add the card to the list of cards showing this turn
    this_turn.append(card_clicked)

    if len(this_turn) == 2:
        # increment the turn counter
        turn_change(1)
    elif len(this_turn) == 3:
        # check if first two were matches, if not hide them again
        if cards[this_turn[0]] != cards[this_turn[1]]:
            exposed[this_turn[0]] = False
            exposed[this_turn[1]] = False
        
        # that turn is over now, get them out of the list
        this_turn.pop(1)
        this_turn.pop(0)

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
