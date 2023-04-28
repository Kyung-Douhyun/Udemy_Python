# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg",30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
import turtle as turtle_module
import random

tim = turtle_module.Turtle()
turtle_module.colormode(255)  # 컬러 모드 rgb 로 변경
color_list = [(15, 20, 39), (162, 62, 41), (198, 161, 108), (140, 162, 192), (230, 204, 99), (45, 14, 10), (34, 13, 21),
              (159, 55, 71), (72, 95, 125), (19, 43, 30), (171, 153, 43), (186, 139, 152), (139, 35, 25), (71, 114, 88),
              (159, 172, 159), (202, 72, 87), (46, 51, 97), (196, 92, 77), (127, 37, 57), (218, 176, 182), (77, 81, 28),
              (41, 81, 43), (225, 175, 171), (88, 112, 176), (176, 189, 213), (44, 73, 75)]
number_of_dot = 100  # 그려질 점의 개수
tim.speed("fastest")  # 터틀 이동 속도 가장 빠르게
tim.pu()
tim.hideturtle()
tim.goto(-250, -250)  # 시작 위치 변경

for dot_count in range(1, number_of_dot + 1):  # 100개의 점을 그리는 반복문, + 1은 100이면 99까지 적용이기 때문에.
    tim.dot(20, random.choice(color_list))  # 점의 크기와 색상 랜덤화
    tim.fd(50)  # 점 생성 후 50만큼 이동
    if dot_count % 10 == 0:  # 만약에 한 줄에 점이 10개가 그려졌다면
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
