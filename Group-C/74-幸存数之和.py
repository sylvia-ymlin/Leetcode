'''
给定一个正整数数列 nums，运算过程：
从 索引 0 的位置开始往后跳，中间跳过 J 个数，命中索引 J+1 的数，该数被敲出，从该点起跳，直到剩余数的个数为 left 个，返回这些数的和

约束：
1. 0 是第一个起跳点
2. 起跳点和被敲出的数中间相隔 jump 个数，不包含起跳点和被敲出的数
3. 跳到末尾时从头循环
4. 如果 left > len(nums) 无需跳数
'''

# 用链表模拟环形结构
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

# 读入数列
nums = list(map(int, input().strip().split(',')))
# 读入 J 和 left
J = int(input().strip())
left = int(input().strip())

n = len(nums)
size = n

if left >= n:
    print(sum(nums))
    exit()

# 构建环形链表
head = Node(nums[0])
head.next = head
head.prev = head
cur = head
for num in nums[1:]:
    new_node = Node(num)
    cur.next = new_node
    new_node.prev = cur
    cur = new_node

cur.next = head # 形成环
head.prev = cur

# 模拟跳跃敲出过程
cur = head # 从第一个节点开始
while size > left:
    # 跳 J 步
    for _ in range(J+1):
        cur = cur.next
    size -= 1
    # print(f"敲出节点值: {cur.val}")
    # print(f"剩余节点数: {size}")
    # 敲出当前节点
    cur.prev.next = cur.next
    cur.next.prev = cur.prev
    cur = cur.prev # 敲出后从前一个节点开始跳

# 计算剩余节点的和
result = 0
cur = head
for _ in range(left):
    result += cur.val
    cur = cur.next

print(result)

