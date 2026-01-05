# 给出一个网络配置列表，每个配置是一个字符串，字符串仅由 数字， ‘*’， ‘？’ 组成。
# 输入用户的 IMSI ，根据下面的规则匹配
# ‘*’： 0 个或多个连续字符
# ‘？’： 下标为奇数的单个字符；下标 0 开始

# 输出所有满足条件的配置，按字典升序，没有返回 null

# 读取网络配置列表
configs = input().split(',')
# 读取用户 IMSI
imsi = input().strip()

# 对每个配置检查是否匹配
# 动态规划，对于 ？ 一定匹配单个字符
# 对 * 选择匹配的数量 -> 即一个 ？ 可以用多次

def is_match(config, imsi, i, j):
    # i, j 分别是 config 和 imsi 的下标
    if i == len(config) and j == len(imsi):
        return True
    if j == len(imsi):
        # imsi 用完了，config 只能剩下 *
        return all(c == '*' for c in config[i:])
    if i == len(config): # config 用完了，imsi 还有，没有匹配完
        return False
    
    if config[i] == '*':
        # 匹配 0 个： i + 1， j 不变
        # 匹配 1 个或多个： i 不变， j + 1
        return is_match(config, imsi, i + 1, j) or is_match(config, imsi, i, j + 1)
    if config[i] == '?': # 只能匹配单个字符，且 j 必须是奇数下标
        if j % 2 == 1:
            return is_match(config, imsi, i + 1, j + 1)
        else:
            return False
    # 普通字符，必须相等
    if config[i] == imsi[j]:
        return is_match(config, imsi, i + 1, j + 1)
    else:
        return False

matched_configs = []
for config in configs:
    if is_match(config, imsi, 0, 0):
        matched_configs.append(config)

if matched_configs:
    matched_configs.sort()
    print(','.join(matched_configs))
else:
    print('null')