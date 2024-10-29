import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib import font_manager

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 使用字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


def draw_cake_with_animation():
    fig, ax = plt.subplots(figsize=(6, 6))

    # 画蛋糕的底层
    bottom_layer = plt.Rectangle((-1.5, -0.5), 3, 0.5, color="sandybrown")
    ax.add_patch(bottom_layer)

    # 画蛋糕的中间层
    middle_layer = plt.Rectangle((-1.2, 0), 2.4, 0.5, color="peachpuff")
    ax.add_patch(middle_layer)

    # 画蛋糕的上层
    top_layer = plt.Rectangle((-0.9, 0.5), 1.8, 0.5, color="moccasin")
    ax.add_patch(top_layer)

    # 画蜡烛的主体
    candle_positions = np.linspace(-0.8, 0.8, 5)
    flames = []

    for i in candle_positions:
        # 蜡烛主体
        candle = plt.Line2D([i, i], [1, 1.3], color="pink", linewidth=3)
        ax.add_line(candle)

        # 初始火焰位置
        flame, = ax.plot([i], [1.35], marker='o', color="orange", markersize=5)
        flames.append(flame)

    # 添加中文祝福语
    ax.text(0, -0.8, '生日快乐!', ha='center', va='center', fontsize=16, color="purple")

    # 调整显示设置
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 1.5)
    ax.axis('off')

    # 定义火焰闪烁的动画
    def update(frame):
        for flame, x in zip(flames, candle_positions):
            # 随机调整火焰的垂直位置和颜色，模拟闪烁
            new_y = 1.35 + 0.05 * np.sin(frame / 2 + np.random.randn())
            flame.set_ydata([new_y])  # 将新的y坐标值放入列表
            flame.set_color("orange" if frame % 2 == 0 else "gold")
        return flames

    ani = animation.FuncAnimation(fig, update, frames=50, interval=100)
    plt.show()


draw_cake_with_animation()
