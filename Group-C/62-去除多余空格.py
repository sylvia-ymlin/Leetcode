# 对于单引号内的内容不做处理
# 否则对于给定坐标范围内的连续多个空格只保留一个
# 输出去除空格后的字符串，和修改后的坐标范围

s = input()
coords_str = input().split(',')
coords = [tuple(map(int, c.split())) for c in coords_str]

# 标记哪些位置在给定范围内
in_range = [False] * len(s)
for start, end in coords:
    for i in range(start, end + 1):
        in_range[i] = True

# 标记要保留的字符
keep = [True] * len(s)
in_quote = False

i = 0
while i < len(s):
    if s[i] == "'":
        in_quote = not in_quote
        i += 1
        continue
    
    # 在范围内 且 不在引号内 且 是空格
    if in_range[i] and not in_quote and s[i] == ' ':
        # 找连续空格的起点
        j = i
        while j < len(s) and s[j] == ' ' and in_range[j] and not in_quote:
            j += 1
        # 保留第一个空格，删除其余
        for k in range(i + 1, j):
            keep[k] = False
        i = j
    else:
        i += 1

# 构建新字符串
new_s = ''.join(s[i] for i in range(len(s)) if keep[i])

# 计算每个位置被删除的字符数（前缀和）
deleted_before = [0] * (len(s) + 1)
for i in range(len(s)):
    deleted_before[i + 1] = deleted_before[i] + (0 if keep[i] else 1)

# 调整坐标
new_coords = []
for start, end in coords:
    new_start = start - deleted_before[start]
    new_end = end - deleted_before[end + 1]
    new_coords.append(f"{new_start} {new_end}")

print(new_s)
print(','.join(new_coords))
    


