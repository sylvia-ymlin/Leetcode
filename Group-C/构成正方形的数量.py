# 输入 n 个 二维坐标，求组成正方形的数量
# 输出正方形的数量

# 题目给出了坐标轴的范围
# 切所有点不重合，所以不会有重复点
# 坐标范围 -10， 10
# 枚举所有点，以这个点为左上角，找右下角的点是否存在，然后再找另外两个点是否存在
# 枚举所有点，以这个点为左顶点，枚举右顶点，找上下两个点是否存在
# 不行，够成正方形的方式有很多种，还是只能用向量的方式判断

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

count = 0
if n < 4:
    print(0)
    exit(0)

# 成对遍历所有点，假设这两个点是一个正方形的对角线，判断另外两个点是否存在
# 对于每一对点 (x1, y1), (x2, y2)
# 和它构成正方形的另外两个点是
# 找到中点，半对角线向量旋转 90 度
# 中点 (mx, my) = ((x1 + x2) / 2, (y1 + y2) / 2)
# 半对角线向量 (dx, dy) = ((x2 - x1) / 2, (y2 - y1) / 2)
# 旋转 90 度后得到两个点
# 点3: (mx - dy, my + dx)
# 点4: (mx + dy, my - dx)

for i in range(n):
    x1, y1 = points[i]
    for j in range(i + 1, n):
        x2, y2 = points[j]
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        dx = (x2 - x1) / 2
        dy = (y2 - y1) / 2
        x3, y3 = mx - dy, my + dx
        x4, y4 = mx + dy, my - dx
        if (x3, y3) in points and (x4, y4) in points:
            count += 1

# 每个正方形被计算了两次，因为每个正方形有两条对角线
print(count // 2)
