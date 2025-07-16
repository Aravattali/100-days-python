import turtle
from turtle import Turtle , Screen
import random
is_race_on = False
from click import prompt

screen = Screen()
screen.setup(width=500 , height=400)
user_bet = screen.textinput("make your bet " , prompt("which turtle will win ? enter color"))
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70 , -40, -10 , 20 , 50, 80 ]
all_turtles = []
turtle.speed("fastest")
for turtle_index in range(0 , 6):
	new_turtle = Turtle(shape="turtle")
	new_turtle.color(colors[turtle_index])
	new_turtle.penup()
	new_turtle.goto(x=-235, y=y_positions[turtle_index])
	all_turtles.append(new_turtle)

if user_bet :
	is_race_on = Turtle
while is_race_on:
	for turtle in all_turtles:
		if turtle.xcor()> 230:
			is_race_on = False
			winning_color = turtle.pencolor()
			if winning_color == user_bet:
				print(f"you've won! the {winning_color} is the winner turtle.")
			else:
				print(f"you've lost. the {winning_color} is the winner turtle.")

		random_distance = random.randint(0 , 10)
		turtle.forward(random_distance)



screen.exitonclick()