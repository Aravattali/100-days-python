import turtle as turtle_module
import random
from turtle import Screen

turtle_module.colormode(255)
tim =turtle_module.Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")
color_list = [  (133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
	tim.dot(20 , random.choice(color_list))
	tim.forward(50)
	if dot_count % 10 == 0:
		tim.setheading(90)
		tim.forward(50)
		tim.setheading(180)
		tim.forward(500)
		tim.setheading(0)
screen = turtle_module.Screen()
screen.exitonclick()