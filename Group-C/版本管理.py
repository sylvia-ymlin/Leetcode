# 版本号格式： . 分隔
# 找到两个版本号之间可用的最高版本号
# 找到第一个不同的部分进行计算 v2 - v1 + 1
# 后续需要 v2 的每一个分段都是0，否则返回 0

# 输入按 “，” 分隔
v1, v2 = input().replace(',', ' ').split()
v1 = list(map(int, v1.split('.')))
v2 = list(map(int, v2.split('.')))

for i in range(min(len(v1), len(v2))):
    if v1[i] != v2[i] and all(x==0 for x in v2[i+1:]):
        print(v2[i] - v1[i] - 1)
        exit(0)

print(0)
    