# 对同一个文件夹下的文件按照时间顺序进行排序
# 文件夹有层级关系
# 根本问题就是要读取所有文件，然后获取每个文件的修改时间，最后进行排序
# 不会出现相同时间和同名文件

# 题目要求的是对制定文件下的文件排序，所以给出的文件结构可能包含其他不需要排序的文件夹
# 读到指定文件夹时，获取该文件夹的层级，然后读取该层级下的所有文件 -> 直到遇到同级的文件夹结束；或者全部读完


n = int(input())
file_list = []
# 目标文件夹名
goal = input().strip()
start = False

for _ in range(n):
    # 需要判断当前是文件夹还是文件
    line = input().strip()
    # 最后一位是 -1 表示文件夹，否则是文件
    if line.endswith(' -1'):
        # 读取文件夹名
        folder_name = line[:-3].strip().lstrip('-')
        if folder_name == goal:
            # 判断当前文件夹的层级
            goal_level = (len(line) - len(line.lstrip('-'))) // 4
            start = True
        elif start:
            # 判断当前文件夹的层级
            curr_level = (len(line) - len(line.lstrip('-'))) // 4
            if curr_level <= goal_level:
                # 已经到达同级文件夹，不再处理后面的，但是还要继续读完输入
                start = False
    elif start: # 是文件，且进入了目标文件夹
    # 是文件，获取文件名和修改时间, 去掉前面所有的“-”
        file_info = line.lstrip('-').split()
        file_name = file_info[0]
        mod_time = int(file_info[1])
        file_list.append((file_name, mod_time))

if not file_list:
    print("No file")
    exit()

# 按照修改时间排序
file_list.sort(key=lambda x: x[1])
# 重新组合文件名和修改时间
for file_name, mod_time in file_list:
    print(f"{file_name} {mod_time}")

# 5
# Documents
# Documents -1
# ----file1.txt 1600000000
# ----file2.txt 1600000100
# ----SubFolder1 -1
# --------file3.txt 1600002000

# 5
# Video
# Video -1
# ----SubFolderO -1
# ----SubFolder1 -1
# ----SubFolder3 -1
# —-------SubFolder4 -1