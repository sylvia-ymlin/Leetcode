# 一座堤坝溃坝，用一批木材填补堤坝缺口
# 求出使得填补面积最大，木材使用数量最少的方案
# 每个溃口只能填补一个木材

n = int(input().strip()) # 坝口数组的长度
# 坝口数组
damages = list(map(int, input().strip().split(',')))
# 木材数组长度
m = int(input().strip())
# 木材数组
woods = list(map(int, input().strip().split(',')))

# 计算缺口深度
base_h = damages[0]
gaps = []
for i in range(1, n-1):
    gaps.append(base_h - damages[i])

# 排序缺口面积和木材高度
gaps.sort(reverse=True) # 缺口面积从大到小
woods.sort() # 木材高度从小到大

usde = [False] * m
total_height = 0

# 贪心匹配
# 优先找能填满的最短木材，找不到就找最长的木材
for gap in gaps:
    best_fit = -1
    for j in range(m):
        if not usde[j] and woods[j] >= gap:
            best_fit = j
            break
    if best_fit == -1:
        for j in range(m-1, -1, -1):
            if not usde[j]:
                best_fit = j
                break
    
    # 除非没有木材了，否则一定能找到
    if best_fit == -1:
        break

    usde[best_fit] = True
    total_height += woods[best_fit]

print(total_height)