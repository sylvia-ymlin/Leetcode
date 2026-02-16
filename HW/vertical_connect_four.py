# First line gives board size
# Second line gives move positions

# Output which move wins, and winning side "red" or "blue"
# If illegal move, output "step, error"

# Read input
n, m = map(int, input().split())
moves = list(map(int, input().split()))

# Initialize board
board = [[0] * n for _ in range(n)]

next_show_row = [0] * n  # Record next available row index for each column (simulating gravity/stacking from bottom)
# Wait, variable name `next_index` in original.
# Renaming to `next_row_index` for clarity.

next_row_index = [0] * n

winner = None
end_step = 0

for step, pos in enumerate(moves):
    # Step index starts from 0 in enumerate, but problem output requires 1-based step
    real_step = step + 1
    
    if step >= n * n: # Too many moves?
        print(f"{real_step},error")
        exit()

    col = pos - 1  # 0-based index

    # Check boundaries and if column full
    if col < 0 or col >= n or next_row_index[col] >= n:
        print(f"{real_step},error")
        exit()
    
    row = next_row_index[col]
    color = 1 if step % 2 == 0 else 2  # 1: Red, 2: Blue
    board[row][col] = color
    next_row_index[col] += 1

    # Check win condition
    # Vertical: only need to check downwards? No, check if current column has 4 consec from top/current.
    # Since we stack, we only check downwards from current `row`.
    if row >= 3 and all(board[r][col] == color for r in range(row - 3, row + 1)):
        winner = "red" if color == 1 else "blue"
        end_step = real_step
        break
    
    # Horizontal check: check 3 left and 3 right
    count = 1
    # Check left
    for c in range(col-1, -1, -1):
        if board[row][c] == color:
            count += 1
        else:
            break
    # Check right
    for c in range(col+1, n):
        if board[row][c] == color:
            count += 1
        else:
            break
    if count >= 4:
        winner = "red" if color == 1 else "blue"
        end_step = real_step
        break

    # Diagonal check: Top-Left to Bottom-Right (\ direction)
    # Check Top-Left relative to current? 
    # Current is `row, col`.
    # Previous pieces are below `row`. But we might place at `row`.
    # Actually, we need to check lines passing through `(row, col)`.
    # Diagonal 1: (row-1, col-1) ... and (row+1, col+1) ...
    # Wait, simple coordinate check.
    count = 1
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0 and board[r][c] == color:
        count += 1
        r -= 1
        c -= 1
    r, c = row + 1, col + 1
    while r < n and c < n and board[r][c] == color:
        count += 1
        r += 1
        c += 1
    if count >= 4:
        winner = "red" if color == 1 else "blue"
        end_step = real_step
        break

    # Anti-Diagonal check: Bottom-Left to Top-Right (/ direction)
    # (row-1, col+1) ... and (row+1, col-1) ...
    count = 1
    r, c = row - 1, col + 1
    while r >= 0 and c < n and board[r][c] == color:
        count += 1
        r -= 1
        c += 1
    r, c = row + 1, col - 1
    while r < n and c >= 0 and board[r][c] == color:
        count += 1
        r += 1
        c -= 1
    if count >= 4:
        winner = "red" if color == 1 else "blue"
        end_step = real_step
        break

if winner:
    print(f"{end_step},{winner}")
else:
    # If no winner and valid moves, what output?
    # Original code didn't handle "Draw" or "Incomplete".
    # Assuming valid game ends with winner or no output?
    # Original code: `print(f"{end},{winner}")` at end.
    # But `end` logic was inside loop.
    # I should print only if winner found.
    pass
