# 误码率：在多少位数据中出现一位差错
# 比特误码率 = 错误比特数/传输总比特数
# 正确传输字符和错误传输压缩存储
# 计算比特误码率

# 用例保证解压后长度一致，即只需要对比相同位置上的元素，不需要考虑插入或删除的情况

s1 = input().strip()  # 传输前
s2 = input().strip()  # 传输后

# 解析压缩字符串：格式为 数字+字符
def parse_compressed_string(s: str) -> list:
    bits = []
    i = 0
    n = len(s)
    while i < n:
        # 先读数字
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        # 再读字符
        char = s[i] if i < n else ''
        i += 1
        bits.append((char, num))  # 存储为 (字符, 数量)
    return bits

s1_bits = parse_compressed_string(s1)
s2_bits = parse_compressed_string(s2)
total_bits = sum(count for _, count in s1_bits)  # 总比特数

# 双指针比较
idx1 = 0  # s1_bits 的索引
idx2 = 0  # s2_bits 的索引
remain1 = s1_bits[0][1]  # 当前字符是否还有剩余位数
remain2 = s2_bits[0][1]  # 没有需要移动到下一个字符
error_bits = 0

# 展开后长度相等，其实不会出现某一方先结束的情况
while idx1 < len(s1_bits) and idx2 < len(s2_bits):
    char1 = s1_bits[idx1][0] # 当前 s1 字符
    char2 = s2_bits[idx2][0] # 当前 s2  字符
    
    # 比较的位数是两者剩余位数的最小值
    compare_bits = min(remain1, remain2)

    # 两个字符要不相等，要不不等
    # 如果字符不同，这些位都是错误的
    if char1 != char2:
        error_bits += compare_bits
    # 相等则直接更新剩余位数
    # 更新剩余位数
    remain1 -= compare_bits
    remain2 -= compare_bits
    
    # 如果某个字符用完了，移动到下一个
    if remain1 == 0:
        idx1 += 1
        if idx1 < len(s1_bits): remain1 = s1_bits[idx1][1] 
    
    if remain2 == 0:
        idx2 += 1
        if idx2 < len(s2_bits): remain2 = s2_bits[idx2][1]

# 计算误码率并保留两位小数
error_rate = error_bits / total_bits
print(f"{error_bits}" + '/' + f"{total_bits}")









    




