#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
Spider = trtl.Turtle()
# The pensize makes a circle which is the spider body.
Spider.pensize(40)
Spider.circle(20)
Spider.goto(20,20)
# This displays how much legs will be there.
Leg = 8
y1 = 70
y2 = y1
leglength = 360 / Leg
print("leglength=", leglength)
Spider.pensize(5)
up = 0
# Tests for how many legs are given and draws however many amounts it is.
while (up < Leg):
  Spider.goto(0,20)
  Spider.setheading(leglength*up - 45)
  Spider.forward(y1)
  print(Leg < y1)
  up = up + 1
Spider.hideturtle()
# Eyes
Spider.penup()
Spider.goto(20,20)
Spider.pendown()
Spider.color("Red")
Spider.circle(0.1)
Spider.penup()
Spider.goto(-20,20)
Spider.pendown()
Spider.circle(0.1)
wn = trtl.Screen()
wn.mainloop()
