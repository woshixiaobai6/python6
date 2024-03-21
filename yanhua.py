import turtle
import random

# 创建画布
canvas = turtle.Screen()
canvas.bgcolor("black")

# 创建烟花粒子类
class Particle(turtle.Turtle):
    def __init__(self, color):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color(color)
        self.penup()

    def explode(self):
        self.shape("circle")
        self.shapesize(0.5)
        self.color("white")

# 创建烟花函数
def create_firework():
    # 随机选择颜色
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    color = random.choice(colors)

    # 创建烟花粒子
    particle = Particle(color)
    particle.goto(0, -200)

    # 设置烟花粒子的初始速度和角度
    speed = random.randint(1, 5)
    angle = random.randint(20, 70)

    # 发射烟花
    while particle.ycor() < 300:
        particle.forward(speed)
        particle.right(angle)
        particle.speed(0)

    # 烟花爆炸效果
    particle.explode()

# 创建多个烟花
for _ in range(10):
    create_firework()

# 关闭画布
canvas.exitonclick()