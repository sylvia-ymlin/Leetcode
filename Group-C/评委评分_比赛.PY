import sys
from functools import cmp_to_key

# 定义选手类，包含索引，总分，分数列表
class Player:
    def __init__(self, index, scores):
        self.index = index
        self.scores = scores # 按高低分值排列
        self.total = sum(scores)

# 自定义比较函数，用于排序
def compare_players(p1, p2):
    if p1.total != p2.total:
        return p2.total - p1.total  # 总分降序
    for s1, s2 in zip(p1.scores, p2.scores): # 各项分数比较
        if s1 != s2:
            return s2 - s1  # 各项分数降序
    return p1.index - p2.index  # 如果全部相等，索引升序

# 主函数
def main():
    try:
        # m 个评委，n 个选手
        m, n = map(int, input().replace(',', ' ').split())
        if not (3 <= n <= 100 and 3 <= m <= 10):
            print(-1)
            return

        scores = [list(map(int, input().replace(',', ' ').split())) for _ in range(m)]
        
        players = []
        # 每一行代表一个评委对所有选手的评分
        for i in range(m):
            if len(scores[i]) != n:
                print(-1)
                return
        
        for j in range(n):
            player_scores = [scores[i][j] for i in range(m)]
            players.append(Player(j, sorted(player_scores, reverse=True)))
        
        players.sort(key=cmp_to_key(compare_players))
        print(','.join(str(player.index + 1) for player in players[:3]))

    except Exception:
        print(-1)

if __name__ == "__main__":
    main()