# import package and making object
import turtle
screen = turtle.Screen()

# method to draw ellipse
def draw(rad):
	
# rad --> radius for arc
	for i in range(2):
		turtle.circle(rad,90)
		turtle.circle(rad//2,90)

# Main Section
# Set screen size
screen.setup(500,500)

# Set screen color
screen.bgcolor('black')

# Colors
col=['violet','blue','green','yellow',
	'orange','red']

# some integers
val=10
ind=0

# turtle speed
turtle.speed(100)

# loop for multiple ellipse
for i in range(36):
	
	# oriented the ellipse at angle = -val
	turtle.seth(-val)
	
	# color of ellipse
	turtle.color(col[ind])
	
	# to access different color
	if ind==5:
		ind=0
	else:
		ind+=1
	
	# calling method
	draw(80)
	
	# orientation change
	val+=10

# for hiding the turtle
turtle.hideturtle()
wait = input()
