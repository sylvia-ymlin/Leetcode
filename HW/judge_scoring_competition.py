import sys
from functools import cmp_to_key

# Define Player class, containing index, total score, score list
class Player:
    def __init__(self, index, scores):
        self.index = index
        self.scores = scores # Sorted by score value high to low
        self.total = sum(scores)

# Custom comparison function for sorting
def compare_players(p1, p2):
    if p1.total != p2.total:
        return p2.total - p1.total  # Total score descending
    for s1, s2 in zip(p1.scores, p2.scores): # Compare individual scores
        if s1 != s2:
            return s2 - s1  # Individual score descending
    return p1.index - p2.index  # If all equal, index ascending

# Main function
def main():
    try:
        # m judges, n players
        m, n = map(int, input().replace(',', ' ').split())
        if not (3 <= n <= 100 and 3 <= m <= 10):
            print(-1)
            return

        scores = [list(map(int, input().replace(',', ' ').split())) for _ in range(m)]
        
        players = []
        # Each row represents one judge's scores for all players
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