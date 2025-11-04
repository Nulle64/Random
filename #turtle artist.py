#turtle artist
#Author: Eric Wang
#oct 28

import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
turtle.bgcolor("black")

colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan"]

def recursive_pinwheel(size, depth):
    if depth == 0 or size < 10:
        return
    
    for i in range(4):  # 4 arms of the pinwheel
        t.forward(size)
        t.right(30)  # slight rotation for spiral effect
        
        # Draw smaller recursive pinwheel first
        recursive_pinwheel(size / 2, depth - 1)
        
        t.left(30)
        t.backward(size)
        t.right(90)  # rotate for next arm
    
    # Draw the current arm color after recursion
    t.color(colors[depth % len(colors)])
    t.forward(size)
    t.backward(size)

# Start drawing
t.penup()
t.setposition(0, 0)
t.pendown()
recursive_pinwheel(100, 5)

turtle.done()











