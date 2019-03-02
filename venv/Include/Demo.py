# 绘制奥运五环
'''奥运五环坐标
1、画笔蓝色-blue-yellow-black-green-red
2、画笔宽度width=10
3、圆环半径r=100  两圆相离120
4、点坐标：（0.-45）（-260，-45）（260，-45）（-130，-155) (130，-155)'''
import turtle
turtle.width(20)
turtle.color("blue")
turtle.penup()
turtle.goto(-260,-45)
turtle.pendown()
turtle.circle(100)
turtle.color("yellow")
turtle.penup()
turtle.goto(-130,-135)
turtle.pendown()
turtle.circle(100)
turtle.color("black")
turtle.penup()
turtle.goto(0,-45)
turtle.pendown()
turtle.circle(100)
turtle.color("green")
turtle.penup()
turtle.goto(130,-155)
turtle.pendown()
turtle.circle(100)
turtle.color("red")
turtle.penup()
turtle.goto(260,-45)
turtle.pendown()
turtle.circle(100)
turtle.done()
