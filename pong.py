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
    
    # reset the scores
    score1 = 0
    score2 = 0
    
    spawn_ball(get_random_direction())

def get_random_direction():
    val = random.randrange(0, 2)
    if val == 0:
        return "LEFT"
    else:
        return "RIGHT"
  
def get_random_velocity():
    x = random.randrange(120, 240)
    y = random.randrange(60, 180)
    return [x, y]

def vector_add(point, vector):
    x = point[0] + vector[0]
    y = point[1] + vector[1]
    return [x, y]

def reflect(vector, edge):
    if edge == "VERTICAL":
        return [vector[0], -vector[1]]
    elif edge == "HORIZONTAL":
        if vector[0] > 0:
            return [-1 * (vector[0] + 1), vector[1]]
        else:
            return [-1 * (vector[0] - 1), vector[1]]
    else:
        # should neven happen
        return vector

def move_paddle(pos, vel):
    pos[1] += vel[1]
    if pos[1] < HALF_PAD_HEIGHT:
        pos[1] = HALF_PAD_HEIGHT
        vel[1] = 0
    if pos[1] > HEIGHT - HALF_PAD_HEIGHT:
        pos[1] = HEIGHT - HALF_PAD_HEIGHT
        vel[1] = 0
    
    return pos
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos = vector_add(ball_pos, ball_vel)
    
    # check for top/bottom wall collision
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel = reflect(ball_vel, "VERTICAL")
    
    # check for gutter collision
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH or ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        # hit the gutter, did it hit a paddle
        if ball_vel[0] > 0 and (ball_pos[1] < paddle2_pos[1] - HALF_PAD_HEIGHT or ball_pos[1] > paddle2_pos[1] + HALF_PAD_HEIGHT):          
            # score player 1
            score1 += 1
            spawn_ball("LEFT")
        elif ball_vel[0] < 0 and (ball_pos[1] < paddle1_pos[1] - HALF_PAD_HEIGHT or ball_pos[1] > paddle1_pos[1] + HALF_PAD_HEIGHT):
            # score  player 2
            score2 += 1
            spawn_ball("RIGHT")
        else:
            # reflect
            ball_vel = reflect(ball_vel, "HORIZONTAL")
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    move_paddle(paddle1_pos, paddle1_vel)
    move_paddle(paddle2_pos, paddle2_vel)
        
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos[1] + PAD_HEIGHT/2], [PAD_WIDTH, paddle1_pos[1] + PAD_HEIGHT/2], [PAD_WIDTH, paddle1_pos[1] - PAD_HEIGHT/2], [0, paddle1_pos[1] - PAD_HEIGHT/2]], 1, "White", "White")
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos[1] + PAD_HEIGHT/2], [WIDTH, paddle2_pos[1] + PAD_HEIGHT/2], [WIDTH, paddle2_pos[1] - PAD_HEIGHT/2], [WIDTH - PAD_WIDTH, paddle2_pos[1] - PAD_HEIGHT/2]], 1, "White", "White")
    
    # draw scores
    canvas.draw_text(str(score1), [WIDTH/2 - 70, 50], 36, "White", "monospace")
    canvas.draw_text(str(score2), [WIDTH/2 + 50, 50], 36, "White", "monospace")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] -= 2
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] += 2
    elif key == simplegui.KEY_MAP["w"]:        
        paddle1_vel[1] -= 2
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] += 2
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0
    elif key == simplegui.KEY_MAP["w"]:        
        paddle1_vel[1] = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 200)


# start frame
new_game()
frame.start()
