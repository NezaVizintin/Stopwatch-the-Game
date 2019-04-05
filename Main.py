# define global variables
import simplegui
time = 0
score_wins = 0
score_total = 0
stopwatch_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    if time == 0:
        string_stopwatch = '0:00.0'
    else:
        minutes = time/600    
        seconds = (time/10)%60
        deciseconds = time%10
        
        deciseconds = str(deciseconds)
        if seconds < 10:
            seconds = '0' + str(seconds)
        else:
            seconds = str(seconds)
        minutes = str(minutes)
        string_stopwatch = minutes + ':' + seconds + '.' + deciseconds

    return string_stopwatch

# define helper fnction that keeps score

def score():
    return str(score_wins) + '/' + str(score_total)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global stopwatch_running
    timer.start()
    stopwatch_running = True
    
def stop_handler():
    global score_total, score_wins, stopwatch_running
    timer.stop()
    if stopwatch_running == True:
        score_total += 1
        if time % 10 == 0:
            score_wins += 1
    stopwatch_running = False
    
def reset_handler():
    timer.stop()
    global time, score_total, score_wins
    time = 0
    score_total = 0
    score_wins = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw_handler (canvas):
    # stopwatch:
    canvas.draw_text(format(time), (150, 200), 40, 'Yellow')
    #score:
    canvas.draw_text(score(), (300, 40), 30, 'Red') 

    
# create frame
frame = simplegui.create_frame('Stop-watch game', 400, 400, 300)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
draw_stopwatch = frame.set_draw_handler(draw_handler)
button_start = frame.add_button('Start', start_handler)
button_stop = frame.add_button('Stop', stop_handler)
button_reset = frame.add_button('Reset', reset_handler)

# start frame
frame.start()
