#import libraries
import turtle
import sys

pen_down = True
direction = None

#function that runs the game
def etch_a_sketch(width, height):
    
    #set canvas size, pen speed and position
    turtle.setup(width=width, height=height)
    turtle.speed(10)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    turtle.listen()

    #run functions when keys are pressed
    turtle.onkey(toggle_pen, 'p')
    turtle.onkey(quit_game, 'q')
    
    turtle.onkeypress(up, 'w')
    turtle.onkeypress(left, 'a')
    turtle.onkeypress(down, 's')
    turtle.onkeypress(right, 'd')

    turtle.onkey(release, 'w')
    turtle.onkey(release, 'a')
    turtle.onkey(release, 's')
    turtle.onkey(release, 'd')

    #teleport the cursor when it reaches an edge
    try:
        while True:
            turtle.update()

            if direction:
               
                if turtle.xcor() < -width / 2:
                    turtle.penup()
                    turtle.goto(width / 2, turtle.ycor())
                    turtle.pendown()
                    
                elif turtle.xcor() > width / 2:
                    turtle.penup()
                    turtle.goto(-width / 2, turtle.ycor())
                    turtle.pendown()
                    
                elif turtle.ycor() < -height / 2:
                    turtle.penup()
                    turtle.goto(turtle.xcor(), height / 2)
                    turtle.pendown()
                    
                elif turtle.ycor() > height / 2:
                    turtle.penup()
                    turtle.goto(turtle.xcor(), -height / 2)
                    turtle.pendown()

                #move cursor based on key press
                if pen_down:

                    if direction == 'w':
                        turtle.sety(turtle.ycor() + 10)

                    elif direction == 'a':
                        turtle.setx(turtle.xcor() - 10)
                    
                    elif direction == 's':
                        turtle.sety(turtle.ycor() - 10)

                    elif direction == 'd':
                        turtle.setx(turtle.xcor() + 10)

    except turtle.Terminator:
        pass

#function that lifts pen up or down
def toggle_pen():
    global pen_down
    pen_down = not pen_down

#function that quts game
def quit_game():
    turtle.bye()

#function that moves pen up
def up():
    global direction
    direction = 'w'

#function that moves pen left
def left():
    global direction
    direction = 'a'

#function that moves pen down
def down():
    global direction
    direction = 's'

#function that moves pen right
def right():
    global direction
    direction = 'd'

#function that releases pen
def release():
    global direction
    direction = None

if __name__ == "__main__":
    # Set default window size if no arguments are provided
    if len(sys.argv) == 1:
        width, height = 1000, 1000
    elif len(sys.argv) == 3:
        width, height = int(sys.argv[1]), int(sys.argv[2])
    else:
        print("Usage: python etchasketch.py [width height]")
        sys.exit(1)

    etch_a_sketch(width, height)
