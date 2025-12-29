# 一天 24 小时
# 注册各个 app 可以使用的时间段，一个时间段只能被一个 app 占用
# 时间段冲突的 app，只能保留一个，优先级高的 app 保留，优先级相同，保留先注册的 app
# 输入一个时间点，返回改时间点可以使用的 app，如果没有，返回 NA

n = int(input().strip()) # app 数量
time_slots = [] # 存储时间段和对应的 app 名称
for i in range(n):
    app_info = input().split()
    app_name = app_info[0]
    app_priority = int(app_info[1])
    start_time = app_info[2]
    end_time = app_info[3]
    # 时间格式固定，可以字典排序
    if start_time < end_time:
        time_slots.append((start_time, end_time, app_name, app_priority))

# 读入要查询的时间点
query_time = input().strip()

# 找到覆盖目标时间点的时间段对应的 app
res = None
for slot in time_slots:
    start_time, end_time, app_name, app_priority = slot
    
    if not res:
        res = [start_time, end_time, app_name, app_priority]
        continue

    # 判断优先级
    existing_start, existing_end, existing_app, existing_priority = res
    if app_priority <= existing_priority:
        continue # 优先级低或相同，跳过

    # 判断是否有冲突，有冲突：包含查询时间点，替换；不包含，置空
    if not(end_time < existing_start or start_time > existing_end):
        if start_time <= query_time < end_time: # 包含起始，不包含结束
            res = [start_time, end_time, app_name, app_priority]
        else:
            res = None
        
print(res[2] if res else "NA")