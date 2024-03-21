import pygame
import random

# 初始化Pygame
pygame.init()

# 设置游戏窗口尺寸
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# 定义颜色
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# 蛇的初始位置和速度
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_speed = [10, 0]

# 食物的初始位置
foods = [[random.randrange(1, (window_width//10)) * 10, random.randrange(1, (window_height//10)) * 10] for _ in range(3)]

# 游戏主循环
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # 检测按键操作
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        snake_speed = [10, 0]
    if keys[pygame.K_LEFT]:
        snake_speed = [-10, 0]
    if keys[pygame.K_UP]:
        snake_speed = [0, -10]
    if keys[pygame.K_DOWN]:
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
            foods.remove(food)
            foods.append([random.randrange(1, (window_width//10)) * 10, random.randrange(1, (window_height//10)) * 10])

    if len(foods) < 3:
        foods.append([random.randrange(1, (window_width//10)) * 10, random.randrange(1, (window_height//10)) * 10])
    else:
        snake_body.pop()

    # 绘制游戏界面
    window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(window, white, pygame.Rect(pos[0], pos[1], 10, 10))
    for food in foods:
        pygame.draw.rect(window, green, pygame.Rect(food[0], food[1], 10, 10))

    # 刷新屏幕
    pygame.display.update()
    
    # 控制游戏速度
    clock.tick(20)

pygame.quit()
