# import package
import turtle
 
# method to draw ellipse
def draw(rad):
     
  # rad --> radius of arc
  for i in range(2):
     
    # two arcs
    turtle.circle(rad,90)
    turtle.circle(rad//2,90)
 
# Main section
# tilt the shape to negative 45
turtle.seth(-45)
 
# calling draw method
draw(100)

wait = input()
