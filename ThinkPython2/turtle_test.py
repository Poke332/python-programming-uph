import turtle
import math

bob = turtle.Turtle()
print(bob)

def polygon(t, length, n):
  for i in range(n):
    t.fd(length)
    t.lt(360/n)

def circle(t, r):
  circumference = 2 * math.pi * r  
  n = int(circumference / 3) + 3
  length = circumference / n
  polygon(t, length, n)    
    

circle(bob, 100)
turtle.mainloop()

