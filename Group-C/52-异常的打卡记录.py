# 异常打卡：
# 1. 实际设备号和注册设备号不同
# 2. 统一员工两个打卡记录时间小于 60 分钟，且距离超过 5km

# 第一行输出打卡记录的条数
# 第二行开始输入打卡记录：工号，时间，打卡距离，实际设备号，注册设备号

# 按照输入顺序，输出异常打卡记录， “；” 分隔
# 没有输出 “null”

n = int(input())
records = [input().split(',') for _ in range(n)]
# 排序，按照工号和时间
# 需要按照输入顺序输出异常打卡记录，所以需要添加 索引
records = [(i, *records[i]) for i in range(n)] # 这里需要用 * 展开 records[i]
records.sort(key=lambda x: (x[1], x[2]))

cur_id = records[0][1]
unusual_records = set()
i = 0
while i < len(records):
    # 判断设备号
    if records[i][4] != records[i][5]:
        unusual_records.add(records[i])
    
    # 检查和上一条是否是同一个人
    if i > 0 and records[i][1] == records[i-1][1]:
        # 计算时间和距离
        diff_time = int(records[i][2]) - int(records[i-1][2])
        diff_dist = abs(int(records[i][3]) - int(records[i-1][3]))
        # 判断时间和距离
        if diff_time < 60 and diff_dist > 5:
            if records[i-1] not in unusual_records: # 避免重复添加
                unusual_records.add(records[i-1])
            unusual_records.add(records[i])
    i += 1 # 移动到下一条记录
    

# 按照 index 排序，恢复输入顺序
unusual_records = list(unusual_records)
unusual_records.sort(key=lambda x: x[0])
# 去掉 index
unusual_records = [r[1:] for r in unusual_records]
# 输出
print(";".join(",".join(r) for r in unusual_records) if unusual_records else "null")
    