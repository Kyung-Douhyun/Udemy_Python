# Create a snake body
# Move the snake
# Create snake food
# Detect collision with food
# Create a scoreboard
# Detect collision with wall
# Detect collision with tail
import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Crate a snake body

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# screen.onkey(snake.down,"Down")
# screen.onkey(snake.left,"Left")
# screen.onkey(snake.right,"Right")
# starting_position = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
# for position in starting_position:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.pu()
#     new_segment.goto(position)
#     segments.append(new_segment)
# Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # 마지막 세그먼트의 위치를 앞 세그먼트의 위치로 이동시키는 코드, 모든 세그먼트는 가장 처음 세그먼트를 제외하고 앞의 세그먼트를 따라간다.
    # for seg_num in range(len(segments) - 1, 0, -1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    # segments[0].fd(20)
    snake.move()

screen.exitonclick()
