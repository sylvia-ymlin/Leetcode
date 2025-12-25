# 从一组数中，找到子数组，数组和可以被 m 整除
# 能找到输出 1， 找不到输出 0

'''
    滑动窗口解决的是量的大小问题，
    前缀和解决的是量之间的关系问题 -> 取模，差，和
'''
# 非单调关系，使用前缀和
# 找两个前缀和的差能被 m 整除

# 输入 n 和 m
n, m = map(int, input().split())
# 输入数组
arr = list(map(int, input().split()))

# 计算前缀和, 并记录每个前缀和 mod m 的余数
# 因为只需要判断是否存在，所以只需要记录余数是否出现过 <- 重点！！！

mod = set()
prefix_sums = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sums[i] = (prefix_sums[i - 1] + arr[i - 1])
    if prefix_sums[i] % m in mod:
        print(1)
        exit(0)
    mod.add(prefix_sums[i] % m)

print(0)