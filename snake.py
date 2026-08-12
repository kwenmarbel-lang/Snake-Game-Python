#Snake Class:
#Method: Create snake ()
#Method: Move snake ()

from turtle import Turtle
import random
class Snake:
    def __init__(self):
      self.turtules =[]
      self.position =[(-40,0),(-20,0),(0,0)]
      self.create_snake()
      self.head = self.turtules[-1]
    def create_snake(self):
        for i in range(len(self.position)):
           new_turtle = Turtle("square")
           new_turtle.color("white")
           new_turtle.penup()
           new_turtle.goto(self.position[i])
           self.turtules.append(new_turtle)
    def extend(self):
          new_segment = Turtle("square")
          new_segment.color("white")
          new_segment.penup()
          new_segment.goto(self.turtules[0].pos())
          self.turtules.insert(0, new_segment)
    def move(self):
          for i in range(len(self.turtules)-1):
              self.turtules[i].goto(self.turtules[i+1].pos())
          self.turtules[-1].forward(20)
    def up(self):
         self.head.setheading(90)
    def down(self):
         self.head.setheading(270)
    def left(self):
         self.head.setheading(180)
    def right(self):
         self.head.setheading(0)