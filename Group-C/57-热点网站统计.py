# 统计 Top N 访问的页面
# 输入
# 每行都是一个 url 或一个数字，如果是 url 代表一段时间内的网页访问
# 如果是一个数字 N，代表本次需要输出的 Top N 个 url（当前数字之前的所有 url 访问次数统计结果）

# 总网页数量小于 5000 个，单网页访问次数小于 65535 次 -> 数据量不大，可以使用字典统计
# 网页 url 由 数字，点分隔符组成，长度小于 127 字节
# 数字是正整数，小于等于 10 且小于当前总访问网页数

# 对每次输入的数字 N，输出当前访问次数排名前 N 的 url 列表

from collections import defaultdict

# 不能提前打印，会破坏输入流
res = []
try:
    counts = defaultdict(int)
    while True:
        line = input().strip()
        if line.isdigit():
            N = int(line)
            # 输出当前访问次数排名前 N 的 url 列表
            sorted_urls = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            top_n_urls = [url for url, count in sorted_urls[:N]]
            res.append(','.join(top_n_urls))
        else:
            counts[line] += 1
except EOFError:
    pass

for output in res:
    print(output)
