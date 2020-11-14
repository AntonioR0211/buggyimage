#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
Spider = trtl.Turtle()
Spider.pensize(40)
Spider.circle(20)
Leg = 8
y1 = 70
y2 = y1
leglength = 380 / Leg
print("leglength=", leglength)
Spider.pensize(5)
up = 0
while (up < Leg):
  Spider.goto(0,0)
  Spider.setheading(leglength*up)
  Spider.forward(y1)
  print(Leg < y1)
  up = up + 1
Spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
