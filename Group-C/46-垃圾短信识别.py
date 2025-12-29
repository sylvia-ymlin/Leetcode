# 识别垃圾短信发送者
# 满足以下任意一条即为垃圾短信发送者：
# 1. A 发送的短信的接收人 中，没有给 A 发送过短信的人数 L > 5
# 2. A 发送的短信数 - A 接收的短信数 = M > 10
# 3. 存在 X， A 给 X 发送的短信 - A 收到 x 的短信 > 5

# ID 最大值 100
# 构建一个 100 x 100 的矩阵，matrix[i][j] 表示 i 给 j 发送的短信数，matrix[j][i] 表示 j 给 i 发送的短信数

MAX_ID = 100

matrix = [[0] * (MAX_ID + 1) for _ in range(MAX_ID + 1)]

# 读入第一行是短信数量
# 后面每一行分别是 发送者 ID，接收者 ID
n = int(input().strip())
for _ in range(n):
    sender, receiver = map(int, input().strip().split())
    matrix[sender][receiver] += 1

# 最后给出一个 id，判断是否为垃圾短信发送者，输出 True or False, 以及 L 和 M
target_id = int(input().strip())
# 计算 L 和 M
L = 0 # target_id 的发送对象 没有给 target_id 发送过短信
# 判断条件 3: A 发送 X - X 发送 A > 5 ？
is_spam = False
for j in range(0, MAX_ID + 1):
    if matrix[target_id][j] > 0:
        if matrix[j][target_id] == 0:
            L += 1
        if matrix[target_id][j] - matrix[j][target_id] > 5:
            is_spam = True

M = 0 # target_id 发送的短信数 - 接收的短信数
sent_count = sum(matrix[target_id])
received_count = sum(matrix[i][target_id] for i in range(1, 101))
M = sent_count - received_count

res = 'True' if (L > 5 or M > 10 or is_spam) else 'False'
print(f"{res} {L} {M}")