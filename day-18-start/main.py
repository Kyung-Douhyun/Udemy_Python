import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")


# 거북이의 랜덤 워크
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# 스피로그래프
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

#
#
# angle = [0, 90, 180, 270]
# for _ in range(100):
#     tim.speed(10)
#     tim.color(random_color())
#     tim.width(10)
#     tim.setheading(random.choice(angle))
#     tim.fd(25)
# 연속으로 삼각형, 사각형, 오각형, 육간형, 칠각형, 팔각형, 구각형 그리기

#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.fd(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

# 길이 10 간격의 점선 그리기
# for _ in range(20):
#     tim.fd(10)
#     tim.pu()
#     tim.fd(10)
#     tim.pd()


# 한 변의 길이 100의 사각형 그리기
# for _ in range(4):
#     tim.fd(100)
#     tim.right(90)

# import 종류
# import turtle 1~2가지의 클래스 생성의 경우
# tim = turtle.Turtle()

# from turtle import Turtle 3가지 이상의 클래스 생성의 경우
# tim = Turtle()

# import turtle as t 모듈 이름이 매우 긴 경우
# tim = t.Turtle()


screen = Screen()
screen.exitonclick()
