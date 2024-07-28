import random
import turtle

import colorgram
from turtle import Turtle, Screen
turtle.colormode(255)
#extracting colors
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color= (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list= [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]
timmy_the_turtle = Turtle()

def move_x(x_cor, y_cor):

    timmy_the_turtle.setpos(x_cor, y_cor)
    timmy_the_turtle.dot(20, random.choice(color_list))
    x_cor+=50
    timmy_the_turtle.teleport(x_cor)
    return x_cor

def move_y(y_cor):
    timmy_the_turtle.penup()
    timmy_the_turtle.setpos(0, y_cor)
    timmy_the_turtle.pendown()
y_coordinate= 0


for j in range (0,10):
    move_y(y_coordinate)
    x_coordinate = 0
    for i in range(0,10):
        x_coordinate= move_x(x_coordinate, y_coordinate)
        i+=1
    y_coordinate+=50




screen= Screen()
screen.exitonclick()