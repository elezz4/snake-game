from snakeclass import Snake
from turtle import Turtle, Screen
from scoreboard import Scoreboard
import time
import pygame
from food import Food

pygame.mixer.init()
eat_sound = pygame.mixer.Sound("sounds/eat.wav")
gameover = pygame.mixer.Sound("sounds/gameover.wav")

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_on = True
screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.right, key="d")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) <= 15:
        eat_sound.play()
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() <  -300 or snake.head.ycor() > 300:
        gameover.play()
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameover.play()
            scoreboard.reset()
            snake.reset()
