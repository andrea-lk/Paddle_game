from graphics import Canvas
import random
import time
import numpy as np

# set up the bricks: 

# Dimensions of the canvas
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 600

# Number of bricks in each row
N_BRICK_COLUMNS = 10

# Number of rows of bricks
N_BRICK_ROWS = 10

# Separation between neighboring bricks, in pixels
BRICK_SEP = 4

# Width of each brick, in pixels
BRICK_WIDTH = (CANVAS_WIDTH-BRICK_SEP * (N_BRICK_COLUMNS + 1)) // N_BRICK_COLUMNS

# Height of each brick, in pixels
BRICK_HEIGHT = 10

# Offset of the top brick row from the top of the canvas, in pixels
BRICK_Y_OFFSET = 70

# List of colors for the bricks
COLORS = ['red', 'orange', 'yellow', 'green', 'blue']

# Step 2: Create the bouncing ball

# Radius of the ball in pixels
BALL_RADIUS = 10

# The ball's vertical velocity
VELOCITY_Y = 6.0

# The ball's minimum and maximum horizontal velocity; the bounds of the
# initial random velocity that you should choose (randomly +/-).
VELOCITY_X_MIN = 2.0
VELOCITY_X_MAX = 6.0

# Animation delay or pause time between ball moves (in seconds)
DELAY = 1 / 120

# Stage 3: Create the Paddle

# Dimensions of the paddle
PADDLE_WIDTH = 70
PADDLE_HEIGHT = 15

# How far up the top of the paddle is from bottom of the canvas
PADDLE_Y_OFFSET = 50

# Stage 5: Finishing touches

# Number of turns
N_TURNS = 3



# make brick helper function
def brick_set_up(canvas):
    # width of the whole block of bricks including the gaps
    block_width = ((N_BRICK_COLUMNS * BRICK_WIDTH) +
                   (N_BRICK_COLUMNS - 1) * BRICK_SEP)
    # tells me space between the block and the canvas
    left_spacer = (CANVAS_WIDTH - block_width) / 2


    for row in range(N_BRICK_ROWS):
        for column in range(N_BRICK_COLUMNS):
            color = COLORS[row//2]

            x1 = (BRICK_WIDTH + BRICK_SEP) * column + left_spacer
            y1 = (BRICK_HEIGHT + BRICK_SEP) * row + BRICK_Y_OFFSET
            x2 = x1 + BRICK_WIDTH
            y2 = y1 + BRICK_HEIGHT
            bricks = canvas.create_rectangle(x1, y1, x2, y2, color, "black")



def get_velocity():
    # add min x velocity bc that's the lower bound
    x_velocity = random.random() * (VELOCITY_X_MAX - VELOCITY_X_MIN) + VELOCITY_X_MIN
    # make it positive or negative with equal probability
    # random number from 0 to 1
    temp = random.random()
    # pick random #. 50/50 chance less than 0.5
    if temp < 0.5:
        x_velocity = -1 * x_velocity
    return x_velocity



# bouncing ball function
def bouncing_ball(canvas):
    # make the ball
    x1 = CANVAS_WIDTH // 2
    y1 = CANVAS_HEIGHT // 2
    x2 = x1 + BALL_RADIUS * 2
    y2 = y1 + BALL_RADIUS * 2
    ball = canvas.create_oval(x1, y1, x2, y2, "black")

    change_x = get_velocity()
    change_y = VELOCITY_Y


    return ball, change_x, change_y



def animation_loop(canvas, ball, paddle, brick_counter, change_x, change_y):


    loss = False

    #update paddle
    mouse_x = canvas.get_mouse_x()
    #paddle moves with mouse x value. does not move with y value, so just keep paddle y value
    canvas.moveto(paddle, mouse_x - PADDLE_WIDTH/2,
                  CANVAS_HEIGHT - PADDLE_Y_OFFSET - PADDLE_HEIGHT)


    # moving the ball

    canvas.move(ball, change_x, change_y)
    # get the corners of the ball so we know when it hits the wall
    ball_top_y = canvas.get_top_y(ball)
    ball_bottom_y = ball_top_y + BALL_RADIUS * 2
    ball_left_x = canvas.get_left_x(ball)
    ball_right_x = ball_left_x + BALL_RADIUS * 2

    # make it bounce when it reaches the bottom of Canvas
    if ball_bottom_y > CANVAS_HEIGHT:
        change_y *= -1
        loss = True

    # make it bounce when it hits the top of the canvas
    if ball_top_y < 0:
        change_y *= -1

    # bounce when reaches right side of canvas
    if ball_right_x > CANVAS_WIDTH:
        change_x *= -1

    # make it bounce when reaches left side of canvas
    if ball_left_x < 0:
        change_x *= -1

    #make the ball's coordinates a list
    collider_list = canvas.find_overlapping(ball_left_x,
                                        ball_top_y, ball_right_x, ball_bottom_y)
    #use list to check if ball has collided with anything
    # (only possible to collide w ball, paddle, or bricks
    for obj in collider_list:
        if obj == ball:
            pass
        elif obj == paddle:
            #make sure its positive
            if change_y > 0:
                change_y *= -1

        #if its not ball or paddle, it will be bricks, so delete the bricks
        else:
            canvas.delete(obj)
            change_y *= -1
            #so that only one block deletes per hit
            brick_counter -= 1
            break


    #update and sleep for all animations
    canvas.update()
    time.sleep(DELAY)

    return change_x, change_y, loss, brick_counter


def moving_paddle(canvas):
    # make paddle
    x1 = (CANVAS_WIDTH - PADDLE_WIDTH) // 2
    y1 = CANVAS_HEIGHT - PADDLE_Y_OFFSET - PADDLE_HEIGHT
    x2 = x1 + PADDLE_WIDTH
    y2 = y1 + PADDLE_HEIGHT
    paddle = canvas.create_rectangle(x1, y1, x2, y2, "black", "black")
    return paddle

    #move the paddle. how do i get x location of mouse through animation loop?


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Breakout')
    brick_set_up(canvas)
    brick_counter = N_BRICK_COLUMNS * N_BRICK_ROWS

    paddle = moving_paddle(canvas)

    for i in range(N_TURNS):
        ball, change_x, change_y = bouncing_ball(canvas)
        canvas.wait_for_click()

        loss = False
        while loss == False and brick_counter > 0:
            change_x, change_y, loss, brick_counter = animation_loop(canvas,
                                                                     ball,
                                                                     paddle,
                                                                     brick_counter,
                                                                     change_x,
                                                                     change_y)
        if brick_counter == 0:
            print("You win!!!! ")

            break

        canvas.delete(ball)




    canvas.mainloop()



if __name__ == '__main__':
    main()

