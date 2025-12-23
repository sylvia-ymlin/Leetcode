# 一排 N 个座位
# 一组员工进出
# 保证离开的位置有员工
# 入座员工和其他人保持最大社交距离
# 优先入座序号最小的位置

n = int(input())
# 读入一个 格式为 [1, 1, 1, 1, -4, 1] 的list
ops = eval(input().strip())

# 座位编号 0 ～ n-1
# 用一个链表记录已经被占用的位置
occupied = set()
# 输出的是最后一个人入座的位置
res = -1
for op in ops:
    if op > 0:
        if len(occupied) == n:
            # 座位已满，无法入座
            print(res)
            exit(0)
        # 找到入座的位置
        if len(occupied) == 0:
            res = 0
        else:
            seats = sorted(occupied)
            best_dist = -1
            best_pos = -1
            prev = -1
            max_gap = [0, -1, n] # 记录最大距离，左边界，右边界
            for cur in seats:
                if prev == -1:
                    dist = cur
                    pos = 0
                else:
                    dist = (cur - prev) // 2
                    pos = prev + dist
                if dist > best_dist:
                    best_dist = dist
                    best_pos = pos
                prev = cur
            # 处理最后一个座位到 n-1 的距离
            # 右端区间
            if n - 1 - prev > best_dist:
                best_pos = n - 1
            res = best_pos
        occupied.add(res)
    else:
        # 离开
        leave_pos = -op
        occupied.remove(leave_pos)
# 输出最终占用的位置
print(res)



