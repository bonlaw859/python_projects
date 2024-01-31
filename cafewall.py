#this program draws several different grid patterns
#with spacing, offset, and different sizes using turtle

#import functions

import turtle
import Lab2_functions

#define main

def main():

    #set up environment

    turtle.setworldcoordinates(0, 400, 650, 0)
    turtle.clear()
    turtle.shape('turtle')
    turtle.pencolor('olive drab')
    turtle.fillcolor('sienna')
    turtle.bgcolor('grey')

    #set turtle speed

    turtle.speed(0)

    #draw all grids

    draw_grid(0,0,0,0,1,8,20)
    draw_grid(0,0,50,70,1,10,30)
    draw_grid(2,0,10,150,8,8,25)
    draw_grid(2,10,250,200,6,6,25)
    draw_grid(2,10,425,180,10,10,20)
    draw_grid(0,35,400,20,4,4,35)

    
#define grid drawing function

def draw_grid(mortar, offset, start_x, start_y,rows, cols, size):

    #loop to use row drawing function to draw a number of rows
    #to form a grid

    for row in range(rows):

        #new variable so start_x does not get changed

        current_x = start_x

        #every other row is offset

        current_x = start_x + (offset * (row % 2))

        #every row other than the first has a space between rows

 #       if row > 0:
#          start_y = start_y + mortar
        start_y += mortar

        #draw the rows with updated variables/parameters

        draw_row(current_x, start_y, row*size, cols, size)

#define row drawing function

def draw_row(current_x, start_y, row, cols, size):

    #draw each 'column' or square

    for col in range(cols):

        #every square color is determined by its number compared to col loop

        color = 'black' if col % 2 == 0 else 'white'

        #set x and y variables

        x1=current_x+size*col
        x2=size
        y1=start_y+row
        y2=size

        #draw the squares

        Lab2_functions.draw_rect(x1, y1, x2, y2, color)

        #draw blue 'x' on each black square

        if color == 'black':
            Lab2_functions.draw_line(x1,y1,(x1+size),(y1+size),'blue')
            Lab2_functions.draw_line((x1+size),y1,x1,(y1+size),'blue')

#call main and finish drawing

if __name__ == "__main__":
    main()
    turtle.done()

    
    
