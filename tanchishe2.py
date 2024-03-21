import pygame
import random

# 初始化pygame
pygame.init()

# 设置窗口尺寸和标题
window_width = 800
window_height = 600
pygame.display.set_caption("贪吃蛇")

# 创建游戏窗口
screen = pygame.display.set_mode((window_width, window_height))

# 设置颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# 定义蛇和食物的初始位置和速度
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_speed = [10, 0]
food_pos = [random.randrange(1, (window_width//10)) * 10, random.randrange(1, (window_height//10)) * 10]
foods = [food_pos]

# 创建一个时钟对象
clock = pygame.time.Clock()

# 定义游戏结束函数
def game_over():
    font = pygame.font.SysFont(None, 72)
    text = font.render("游戏结束！", True, red)
    screen.blit(text, ((window_width - text.get_width()) / 2, (window_height - text.get_height()) / 2))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    quit()

# 游戏循环
while True:
    # 处理游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_speed = [-10, 0]
            elif event.key == pygame.K_RIGHT:
                snake_speed = [10, 0]
            elif event.key == pygame.K_UP:
                snake_speed = [0, -10]
            elif event.key == pygame.K_DOWN:
                snake_speed = [0, 10]

    # 移动蛇的身体
    snake_pos[0] += snake_speed[0]
    snake_pos[1] += snake_speed[1]

    # 判断是否超出窗口边界
    if snake_pos[0] >= window_width:
        snake_pos[0] = 0
    elif snake_pos[0] < 0:
        snake_pos[0] = window_width - 10

    if snake_pos[1] >= window_height:
        snake_pos[1] = 0
    elif snake_pos[1] < 0:
        snake_pos[1] = window_height - 10

    snake_body.insert(0, list(snake_pos))

    # 检测蛇是否吃到食物
    for food in foods[:]:
        if snake_pos[0] == food[0] and snake_pos[1] == food[1]:
            # 吃到食物后，不删除食物，让蛇的身体增长一格
            foods.append([random.randrange(1, (window_width//10)) * 10, random.randrange(1, (window_height//10)) * 10])
        else:
            foods.remove(food)

    # 如果蛇头和蛇身体重叠，游戏结束
    if snake_pos in snake_body[1:]:
        game_over()

    # 绘制游戏界面
    screen.fill(white)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    for food in foods:
        pygame.draw.rect(screen, black, pygame.Rect(food[0], food[1], 10, 10))

    pygame.display.update()

    # 控制游戏速度
    clock.tick(20)
