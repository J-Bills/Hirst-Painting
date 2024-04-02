import turtle

import colorgram
import random
from turtle import Turtle, Screen


colors = colorgram.extract('hirst-image.jpg', 6)
color_list = list()

for color in colors:
    rgb_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
    color_list.append(rgb_tuple)

def generate_color():
    random_color = random.choice(color_list)
    return random_color

def dot(size, random_color):
    hirst.dot(20, random_color)
    hirst.forward(size)

def draw():
    for i in range(0,50):
        if hirst.xcor() > 250:
            hirst.lt(90)
            color_val = generate_color()
            dot(50, color_val)
            # hirst.lt(90)
            # color_val = generate_color()
            # dot(50, color_val)
        elif hirst.xcor() < -250:
            print(hirst.xcor())
            hirst.rt(90)
            color_val = generate_color()
            dot(50, "red")
            # hirst.rt(90)
            # color_val = generate_color()
            # dot(50, color_val)
        else:
            color_val = generate_color()
            dot(50, color_val)


def main():
    draw()

window = Screen()
window.colormode(255)
hirst = Turtle()
hirst.teleport(-250, -250)
hirst.penup()
main()
dot(20,'red')
window.exitonclick()




# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.



