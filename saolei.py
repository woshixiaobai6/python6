import pygame
import random

# 游戏参数
ROWS = 10
COLS = 10
MINES = 20
CELL_SIZE = 50
WINDOW_WIDTH = COLS * CELL_SIZE
WINDOW_HEIGHT = ROWS * CELL_SIZE

# 颜色定义
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 初始化游戏面板
def init_board(rows, cols, mines):
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # 随机布置地雷
    mine_indices = random.sample(range(rows * cols), mines)
    for idx in mine_indices:
        row = idx // cols
        col = idx % cols
        board[row][col] = -1
        
        # 更新周围格子的数字
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if 0 <= i < rows and 0 <= j < cols and board[i][j] != -1:
                    board[i][j] += 1
    
    return board

# 绘制游戏界面
def draw_board(screen, board, revealed):
    for row in range(ROWS):
        for col in range(COLS):
            # 绘制格子背景
            pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            
            # 绘制已揭示的数字或地雷
            if revealed[row][col]:
                if board[row][col] == -1:
                    pygame.draw.circle(screen, BLACK, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 4)
                else:
                    number = board[row][col]
                    color = RED if number == 0 else BLACK
                    font = pygame.font.Font(None, CELL_SIZE // 2)
                    text = font.render(str(number), True, color)
                    text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
                    screen.blit(text, text_rect)
            
            # 绘制未揭示的格子边框
            pygame.draw.rect(screen, GRAY, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# 主游戏循环
def main():
    # 初始化游戏
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Minesweeper")
    
    board = init_board(ROWS, COLS, MINES)
    revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]
    
    game_over = False
    
    while True:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                # 鼠标左键点击
                if event.button == 1:
                    x, y = event.pos
                    col = x // CELL_SIZE
                    row = y // CELL_SIZE
                    
                    # 揭示格子
                    revealed[row][col] = True
                    
                    # 点到地雷，游戏结束
                    if board[row][col] == -1:
                        game_over = True
                # 鼠标右键点击，标记地雷
                elif event.button == 3:
                    x, y = event.pos
                    col = x // CELL_SIZE
                    row = y // CELL_SIZE
                    
                    # 标记或取消标记地雷
                    revealed[row][col] = not revealed[row][col]
        
        # 绘制游戏界面
        screen.fill(WHITE)
        draw_board(screen, board, revealed)
        
        # 游戏结束，显示提示信息
        if game_over:
            font = pygame.font.Font(None, 40)
            text = font.render("Game Over!", True, BLACK)
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            screen.blit(text, text_rect)
        
        # 更新屏幕显示
        pygame.display.flip()

# 启动游戏
if __name__ == "__main__":
    main()
