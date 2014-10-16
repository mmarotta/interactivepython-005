# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [1, 1]
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2] 
paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT / 2]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists

    # set the location of the ball in the center of the canvas
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    # set the velocity based on the direction passed in
    if (direction == "LEFT"):
        ball_vel = [-1, -1]
    elif (direction == "RIGHT"):
        ball_vel = [1, -1]
    else:
        # this should never happen...
        ball_vel = [3, -3]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos[1] + PAD_HEIGHT/2], [PAD_WIDTH, paddle1_pos[1] + PAD_HEIGHT/2], [PAD_WIDTH, paddle1_pos[1] - PAD_HEIGHT/2], [0, paddle1_pos[1] - PAD_HEIGHT/2]], 1, "White", "White")
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos[1] + PAD_HEIGHT/2], [WIDTH, paddle2_pos[1] + PAD_HEIGHT/2], [WIDTH, paddle2_pos[1] - PAD_HEIGHT/2], [WIDTH - PAD_WIDTH, paddle2_pos[1] - PAD_HEIGHT/2]], 1, "White", "White")
    
    # draw scores
    canvas.draw_text(str(score1), [WIDTH/2 - 70, 50], 36, "White", "monospace")
    canvas.draw_text(str(score2), [WIDTH/2 + 50, 50], 36, "White", "monospace")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
