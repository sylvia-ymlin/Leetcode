# 给定一个多个命令字组成的命令字符串
# 只包含大小写字母，数字，下划线，偶数个双引号
# 双引号可以标识包含 _ 的命令字 或 空命令字
# 命令字之间用单个或多个下划线连接
# 对指定索引的敏感字段加密，替换为 ******, 删除命令字前后多余的下划线

# 输出两行
# 第一行，命令字索引
# 第二行，要处理的命令字符串

# 输出处理后的命令字符串，无法找到指定索引则输出“ERROR”

# 示例1
# 输入
# 1
# password__a12345678_timeout_100
# 输出
# password_******_timeout_100

index = int(input().strip())
command_str = input().strip()

# 问题在于，如果用 split('_') 直接分割，会把双引号内的下划线也分割掉
# 先用 “” 分割，再处理每个部分
parts = command_str.split('"')
# 带双引号的命令字->奇数
commands = []
for i in range(len(parts)):
    if i % 2 == 0:
        sub_parts = parts[i].split('_')
        for sp in sub_parts:
            if sp != '':
                commands.append(sp)
    else:
        commands.append('"' + parts[i] + '"')

if index < 0 or index >= len(commands):
    print("ERROR")
else:
    commands[index] = '******'
    print('_'.join(commands))