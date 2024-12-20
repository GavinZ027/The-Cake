import turtle
import time
import random

# 创建窗口
screen = turtle.Screen()
screen.title("圣诞树")
screen.bgcolor("black")

# 设置树的主体
tree = turtle.Turtle()
tree.hideturtle()
tree.speed(0)

# 树的参数
layer_height = 60  # 每层高度
base_width = 200  # 树底层的宽度
layers = 4  # 树的层数

# 绘制圣诞树
def draw_tree():
    tree.color("green")
    tree.penup()
    tree.goto(0, -200)
    tree.pendown()

    for i in range(layers):  # 多层树
        tree.begin_fill()
        width = base_width - i * 40
        tree.goto(tree.xcor() - width // 2, tree.ycor())  # 每层从左边开始
        for _ in range(3):  # 每层是一个等边三角形
            tree.forward(width)
            tree.left(120)
        tree.end_fill()
        tree.penup()
        tree.goto(0, tree.ycor() + layer_height)  # 移动到下一层的中心
        tree.pendown()

    # 树干
    tree.color("brown")
    tree.penup()
    trunk_width = base_width // 6  # 树干宽度
    trunk_height = layer_height  # 树干高度
    tree.goto(-trunk_width // 2, -200 - trunk_height)  # 树干居中
    tree.pendown()
    tree.begin_fill()
    for _ in range(2):
        tree.forward(trunk_width)
        tree.left(90)
        tree.forward(trunk_height)
        tree.left(90)
    tree.end_fill()

# 生成灯光位置
def generate_light_positions():
    light_positions = []
    start_y = -200
    for i in range(layers):  # 每层树
        width = base_width - i * 40
        y = start_y + i * layer_height
        for j in range(10):  # 每层生成 10 个灯
            x = random.randint(-width // 2 + 10, width // 2 - 10)
            # 灯光紧贴三角形边界，公式确保灯光位于层的外轮廓
            adjusted_y = y + (layer_height / 2) - (abs(x) / (width / 2)) * (layer_height / 2)
            light_positions.append((x, adjusted_y))
    return light_positions

# 绘制闪烁灯
def add_lights(light_positions):
    light = turtle.Turtle()
    light.hideturtle()
    light.speed(0)
    light.penup()
    colors = ["red", "yellow", "blue", "white", "pink"]

    while True:
        for x, y in light_positions:
            light.goto(x, y)
            light.dot(10, random.choice(colors))
        time.sleep(0.5)
        light.clear()

# 绘制树
draw_tree()

# 生成灯光位置并添加闪烁灯
light_positions = generate_light_positions()
add_lights(light_positions)

# 停留窗口
turtle.done()
