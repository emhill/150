import turtle

def spiral(length, angle):
	if length > 0:
		turtle.forward(length)
		turtle.right(angle)
		spiral(length - 5, angle)

# spiral loop
# make length the loop variable
# draw the same as the recursive version

spiral(100, 45)

turtle.Screen().exitonclick()
