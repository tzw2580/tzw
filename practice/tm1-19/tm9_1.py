# 要求输出国际象棋棋盘。
# ANSI颜色代码
BLACK = "\033[40m  \033[0m"
WHITE = "\033[47m  \033[0m"

size = 8
for row in range(size):
    line = []
    for col in range(size):
        line.append(BLACK if (row + col) % 2 == 0 else WHITE)
    print("".join(line))