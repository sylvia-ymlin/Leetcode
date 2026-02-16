# Given scores of several shooters, sort each player by sum of their top 3 scores in descending order; output sorted player ID sequence
# A player can have multiple shooting scores, and order is not fixed
# If a player has fewer than 3 scores, all scores of the player are invalid, ignore player in ranking
# If scores are equal, sort by ID in descending order

# Sorting problem

# Number of scores
N = int(input())
# This line gives a series of player IDs
# Give scores corresponding to player IDs
ids = list(map(int, input().split(',')))
scores = list(map(int, input().split(',')))

# Use dictionary to count scores for each player
score_dict = {}
for i in range(N):
    id = ids[i]
    score = scores[i]
    if id not in score_dict:
        score_dict[id] = []
    score_dict[id].append(score)

# Iterate through each player, calculate sum of top 3 scores
final_scores = []
for id, score_list in score_dict.items():
    if len(score_list) >= 3:
        top_three_scores = sorted(score_list, reverse=True)[:3]
        total_score = sum(top_three_scores)
        final_scores.append((id, total_score))

# Sort by total score in descending order. If scores equal, sort by ID in descending order
final_scores.sort(key=lambda x: (x[1], x[0]), reverse=True)
# Output player ID sequence
print(','.join(str(item[0]) for item in final_scores))