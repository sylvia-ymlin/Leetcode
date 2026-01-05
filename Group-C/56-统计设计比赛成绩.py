# 给出若干射手的成绩分数，对每个选手按其最高三个分数之和降序排序；输出降序排名后的选手 ID 序列
# 一个选手可以有多个射击成绩，且次序不固定
# 如果选手成绩少于三个，则选手的所有成绩无效，排名忽略该选手
# 成绩相等的按照 ID 降序排列

# 排序问题

# 设计成绩数量
N = int(input())
# 这一行给出一系列选手 id
# 给出选手 id 对应的成绩
ids = list(map(int, input().split(',')))
scores = list(map(int, input().split(',')))

# 用字典，统计每个选手的成绩
score_dict = {}
for i in range(N):
    id = ids[i]
    score = scores[i]
    if id not in score_dict:
        score_dict[id] = []
    score_dict[id].append(score)

# 遍历每个选手，计算其最高三个分数之和
final_scores = []
for id, score_list in score_dict.items():
    if len(score_list) >= 3:
        top_three_scores = sorted(score_list, reverse=True)[:3]
        total_score = sum(top_three_scores)
        final_scores.append((id, total_score))

# 按照总分降序排列，分数相等时按 ID 降序排列
final_scores.sort(key=lambda x: (x[1], x[0]), reverse=True)
# 输出选手 ID 序列
print(','.join(str(item[0]) for item in final_scores))