import turtle

# 设置画布
screen = turtle.Screen()
screen.bgcolor("white")

# 设置画笔
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.penup()

# 第一个图案
t.setpos(0, -150)
t.pendown()
t.pensize(2)
t.fillcolor("#02330C")  # 设置填充颜色
t.begin_fill()
for _ in range(3):
    t.forward(200)
    t.circle(15, 120)
t.end_fill()

# 第二个图案
t.penup()
t.setpos(-60, -50)
t.pendown()
t.fillcolor("#3C4300")
t.begin_fill()
t.left(90)
t.forward(120)
t.right(120)
t.forward(120)
t.right(120)
t.forward(120)
t.end_fill()

# 第三个图案
t.penup()
t.setpos(60, -50)
t.pendown()
t.fillcolor("#556109")
t.begin_fill()
t.right(180)
t.forward(120)
t.left(120)
t.forward(120)
t.left(120)
t.forward(120)
t.end_fill()

# 更新画布
screen.update()
print()

# 结束绘制
turtle.done()
