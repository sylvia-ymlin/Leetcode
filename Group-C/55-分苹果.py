# A, B 把苹果分为两堆

# 输出： 苹果数量，每个苹果重量
n = int(input())
weights = list(map(int, input().split()))

# 输出： B 获得的苹果的总重量
# A 要求按照二进制计算苹果总重量然后均分，计算规则：转换为二进制，不进位
# b 按照正常十进制计算重量
# 要求在满足 a 的前提下， b 获得的重量最大

# 不进位的二进制等于 按位异或
# 计算总重量的异或值，如果为 0，说明可以均分，则取出最小的苹果分给 A，其余分给 B
# 无法满足 a 的要求 -> 不能均分，返回 -1

total_xor = 0
total_sum = 0
for w in weights:
    total_xor ^= w # 计算异或值
    total_sum += w

if total_xor != 0:
    print(-1)
else:
    min_weight = min(weights)
    b_weight = total_sum - min_weight
    print(b_weight)