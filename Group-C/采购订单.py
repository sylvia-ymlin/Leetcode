# 纯模拟问题
import math

def process_order():
    n = int(input())
    if not (2 <= n <= 100): # 验证题目条件
        return 

    # 高价低价单独处理
    high_price_pos = [] # [(item_id, quantity, price), ...]
    low_price_pos = {} # {item_id: [total_quantity, price], ...}

    # 读入订单
    for _ in range(n):
        item_id, quantity, price, status = map(int, input().split())

        # 仅处理状态为 0 的订单
        if status != 0:
            continue

        if price > 100:
            high_price_pos.append((item_id, int(quantity), int(price)))
        else:
            # 单价低于或等于 100 的订单，相同 item_id 可以合并然后打折
            if item_id in low_price_pos:
                low_price_pos[item_id][0] += int(quantity)
            else:
                low_price_pos[item_id] = [int(quantity), int(price)]
            
            
    # 对数量大于 100 的低价订单打 9 折
    for item_id in low_price_pos:
        quantity, price = low_price_pos[item_id]
        if quantity > 100:
            price = math.floor(price * 0.9)
        low_price_pos[item_id][1] = price
    
    # 合并所有订单
    final_orders = []
    for item_id, quantity, price in high_price_pos:
        final_orders.append((item_id, quantity, price))
    for item_id in low_price_pos:
        quantity, price = low_price_pos[item_id]
        final_orders.append((item_id, quantity, price))
    
    # 按照 item_id 升序排序， 数量降序排序
    final_orders.sort(key=lambda x: (x[0], -x[1]))

    # 输出结果
    for item_id, quantity, price in final_orders:
        print(f"{item_id} {quantity} {price}")

    return


if __name__ == "__main__":
    process_order()

