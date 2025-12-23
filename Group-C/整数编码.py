# 对输入的数字，七位一组编码，最高位表示后续是否还有数据
# 输出为编码的十六进制字符串

# 输入一个字符串，表示一个非负整数
num_str = input().strip()
num = int(num_str)
# 转为二进制字符串
bin_str = bin(num)[2:] # 去掉 '0b' 前缀
# 七位一个组，从低位开始分组
res = ""
index = len(bin_str)
# 采用小端编码，所以第一个输出的是最低位
while len(bin_str) > 7:
    group = bin_str[-7:] # 取最后七位
    bin_str = bin_str[:-7] # 去掉最后七位
    group = '1' + group # 最高位设为 1，表示后续还有数据
    res += group

# 最后剩下的部分
group = bin_str.zfill(8) # 前面，包括最高位，全部补0，共8位
res += group
# 二进制字符串转为十六进制，字母要大写
hex_res = ""
for i in range(0, len(res), 8): # 需要按照八位一组转换，一组用两位十六进制表示
    byte = res[i:i+8]
    # 需要二进制先转为十进制，再转为十六进制 hex(int(byte, 2))
    # 去掉 '0x' 前缀 [2:] ，补齐两位 zfill(2)，字母大写 .upper()
    hex_byte = hex(int(byte, 2))[2:].zfill(2).upper()
    hex_res += hex_byte

print(hex_res)


