from turtle import Screen , Turtle
import  time
from snake import Snake

screen = Screen()
screen.setup(600 , 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

is_game_on = True
while is_game_on:
	screen.update()
	time.sleep(0.1)
	snake.move()








screen.exitonclick()