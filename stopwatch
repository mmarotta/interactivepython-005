# "Stopwatch: The Game"
import simplegui

# define global variables
timerValue = 0
isStopwatchRunning = False
gamesWon = 0
gamesPlayed = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    # format the time as M:SS:s
    # Minutes:Seconds:Tenths
    minutes = t / 600
    tens_sec = (t / 100) % 6
    ones_sec = (t / 10) % 10
    frac_sec = t % 10
    
    return str(minutes) + ":" + str(tens_sec) + str(ones_sec) + "." + str(frac_sec)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_handler():
    # start the stopwatch and mark the state that it
    # is running
    global isStopwatchRunning
    timer.start()
    isStopwatchRunning = True
    
def stop_button_handler():    
    global isStopwatchRunning, gamesPlayed, gamesWon
    timer.stop()
    
    # make sure stopwatch was actually running to register a game
    if isStopwatchRunning:
        # increment gamesPlayed
        gamesPlayed += 1
        
        # check if the player won
        # win is tenths of a seconds = 0
        if timerValue % 10 == 0:
            gamesWon += 1
        
    # mark the state as not running
    isStopwatchRunning = False
    
def reset_button_handler():
    # stop the times and reset the stopwatch
    # and game counters
    global timerValue, gamesPlayed, gamesWon, isStopwatchRunning
    timer.stop()
    isStopwatchRunning = False
    timerValue = 0
    gamesWon = 0
    gamesPlayed = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global timerValue
    timerValue += 1
    
timer = simplegui.create_timer(100, timer_handler)

# define draw handler
def draw_handler(canvas):
    # draw the timer
    canvas.draw_text(format(timerValue), [40, 200], 65, "White", "monospace")
    
    # draw the scores 
    canvas.draw_text(str(gamesWon) + " / " + str(gamesPlayed), [150, 50], 35, "Green", "monospace")
    
# create frame
frame = simplegui.create_frame("Stopwatch Game", 300, 300)

# register event handlers
frame.add_button("Start", start_button_handler, 100)
frame.add_button("Stop", stop_button_handler, 100)
frame.add_button("Reset", reset_button_handler, 100)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
