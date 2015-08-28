import turtle

def polystar_even(num_pts, length):
	half_pts = num_pts / 2
	
	for i in range(half_pts):
		turtle.forward(length)
		turtle.right(720 / num_pts)
	
	turtle.penup()
	turtle.left(180/num_pts)
	turtle.forward(length/1.8)
	turtle.right(540/num_pts)
	turtle.pendown()
	
	for i in range(half_pts):
		turtle.forward(length)
		turtle.right(720 / num_pts)

for i in range(6, 18, 2):
	turtle.penup()
	turtle.forward(80)
	turtle.right(360 / 12)
	turtle.pendown()
	polystar_even(i, 20)

turtle.Screen().exitonclick()
