# Key is x moves one by one, when no instruction, y remains unchanged

m, E = map(int, input().split())
moves = []
for _ in range(m):
    moves.append(list(map(int, input().split())))

area = 0
y = 0
idx = 0
for x in range(E):
    if idx < m and x == moves[idx][0]:
        y += moves[idx][1]
        idx += 1
    
    area += abs(y)

print(area)
