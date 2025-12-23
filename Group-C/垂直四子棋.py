# 第一行给出棋盘大小
# 第二行给出落棋位置

# 输出第几个棋子落下后获胜，以及获胜方 "red" 或 "blue"
# 如果出现非法落子，输出 "step, error"

# 读取输入
n, m = map(int, input().split())
moves = map(int, input().split())

# 初始化棋盘
board = [[0] * n for _ in range(n)]

next_index = [0] * n  # 记录每列下一个可落子的位置

for step, pos in enumerate(moves):
    if step >= n * n:
        print(f"{step + 1}, error")
        break

    col = pos - 1  # 转换为 0 基索引

    if col < 0 or col >= n or next_index[col] >= n:
        end = step + 1
        break
    
    row = next_index[col]
    color = 1 if step % 2 == 0 else 2  # 1 表示红色，2 表示蓝色
    board[row][col] = color
    next_index[col] += 1

    # 检查是否获胜
    # 纵向只可能是下面所有都是同色
    if row >= 3 and all(board[r][col] == color for r in range(row - 3, row + 1)):
        winner = "red" if color == 1 else "blue"
        print(f"{step + 1} {winner}")
        break
    # 纵向检查, 左边和右边各检查 3 个
    count = 1
    for c in range(col-1, -1, -1):
        if board[row][c] == color:
            count += 1
        else:
            break
    for c in range(col+1, n):
        if board[row][c] == color:
            count += 1
        else:
            break
    if count >= 4:
        winner = "red" if color == 1 else "blue"
        end = step + 1
        break

    # 斜向检查，左上到右下
    count = 1
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if board[r][c] == color:
            count += 1
            r -= 1
            c -= 1
        else:
            break
    r, c = row + 1, col + 1
    while r < n and c < n:
        if board[r][c] == color:
            count += 1
            r += 1
            c += 1
        else:
            break
    if count >= 4:
        winner = "red" if color == 1 else "blue"
        end = step + 1
        break

    
print(f"{end},{winner}")

