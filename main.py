import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Snake Setup
positions = [(0, 0), (-20, 0), (-40, 0)]

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_status = True

while game_status:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect Contact With The Food
    if snake.head.distance(food) < 15:
        food.new_location()
        snake.extend_snake()
        scoreboard.increase_score()
        scoreboard.update_score()

    # Detect Contact With The Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset()

    # Detect Contact With The Tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
