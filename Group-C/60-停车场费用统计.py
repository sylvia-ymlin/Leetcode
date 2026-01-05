# 包月车不统计
# 不包月： 半小时 1 元；不满半小时不收费；超过半小时，零头不满半小时按半小时计费
# 每天 11:30 - 13:30 不收费
# 超过 8 小时后的不收费

def time_to_minutes(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m

def calculate_cost(enter, leave):
    enter = time_to_minutes(enter)
    leave = time_to_minutes(leave)
    
    # 计算总停车时间
    total_time = leave - enter
    # 扣除免费时间段
    free_start = time_to_minutes('11:30')
    free_end = time_to_minutes('13:30')
    if leave <= free_start or enter >= free_end:
        pass  # 不在免费时间段内
    else:
        overlap_start = max(enter, free_start)
        overlap_end = min(leave, free_end)
        total_time -= (overlap_end - overlap_start)
    total_time = min(total_time, 8 * 60)  # 超过 8 小时不收费
    if total_time < 30:
        return 0
    return (total_time + 29) // 30  # 向上取整，半小时 1 元

# 进出停车场的包月车的数量
n = int(input())
# 包月车牌号
monthly_cars = set(input().split())
# 车辆进出记录: 时间，车牌号，进/出
# 时间格式 HH:MM
records = []

while True:
    line = input()
    if not line:
        break
    time, plate, action = line.split()
    records.append((time, plate, action))


# 用 set 存储车辆的进出
res = 0
cars_info = {}
for time, plate, action in records:
    if plate in monthly_cars:
        continue
    if action == 'enter':
        cars_info[plate] = time
    else:
        enter_time = cars_info[plate]
        res += calculate_cost(enter_time, time)

print(res)

