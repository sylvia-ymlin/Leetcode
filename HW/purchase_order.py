# Pure simulation problem
import math

def process_order():
    n = int(input())
    if not (2 <= n <= 100): # Check condition
        return 

    # Handle high and low price separately
    high_price_pos = [] # [(item_id, quantity, price), ...]
    low_price_pos = {} # {item_id: [total_quantity, price], ...}

    # Read orders
    for _ in range(n):
        item_id, quantity, price, status = map(int, input().split())

        # Only process orders with status 0
        if status != 0:
            continue

        if price > 100:
            high_price_pos.append((item_id, int(quantity), int(price)))
        else:
            # Orders with unit price <= 100, merge same item_id then discount
            if item_id in low_price_pos:
                low_price_pos[item_id][0] += int(quantity)
            else:
                low_price_pos[item_id] = [int(quantity), int(price)]
            
            
    # Apply 10% discount for low price items with quantity > 100
    for item_id in low_price_pos:
        quantity, price = low_price_pos[item_id]
        if quantity > 100:
            price = math.floor(price * 0.9)
        low_price_pos[item_id][1] = price
    
    # Merge all final orders
    final_orders = []
    for item_id, quantity, price in high_price_pos:
        final_orders.append((item_id, quantity, price))
    for item_id in low_price_pos:
        quantity, price = low_price_pos[item_id]
        final_orders.append((item_id, quantity, price))
    
    # Sort by item_id ascending, quantity descending
    final_orders.sort(key=lambda x: (x[0], -x[1]))

    # Output result
    for item_id, quantity, price in final_orders:
        print(f"{item_id} {quantity} {price}")

    return


if __name__ == "__main__":
    process_order()
