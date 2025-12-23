# 将 M 个 列表的元素均分到 N 个窗口中
# 每个窗口需要 K 个元素，来自不同列表
# 需要将每个列表元素尽量均分为 N 份

# 模拟即可

n = int(input())
k = int(input())
elems= []
while True:
    try:
        lst = list(map(int, input().split()))
        elems.append(lst)
    except EOFError:
        break

output_length = [0 for k in range(len(elems))] # 记录每个列表已经输出的元素个数
res = []

# 轮流从列表中取数
# 先取数，输出的时候再计算正确的索引
# 对于当前列表，如果长度足够，则取出 n 个元素
# 长度不够，有多少取多少
# 输出的时候，直接按 n 跳取即可
while True:
    if len(res) >= n * k: # 取够了 N 个窗口，每个 K 个元素
        break
    else:
        # 从每个列表中取数
        for i in range(len(elems)):
            used = output_length[i]
            new_used = min(used + n, len(elems[i]))
            res += elems[i][used:new_used]
            output_length[i] = new_used

output = ""
for i in range(n):
    for j in range(k):
        idx = i + j * n
        output += str(res[idx]) + " "

print(output.strip())

        
        