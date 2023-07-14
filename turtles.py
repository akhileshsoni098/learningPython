from turtle import *
import colorsys

title("Akhilesh Soni")
bgcolor("black")
h = 0
n = 70
speed(0)

for i in range(200):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 1/4
    color(c)
    right(1)
    backward(1)
    for j in range(2):
        right(2)
        circle(200)

done()
