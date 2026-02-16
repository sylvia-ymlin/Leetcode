# A set of cards, order is ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# First line gives cards in hand
# Second line gives cards on table
# Output longest possible straight length for opponent. For same length take largest face value

mines = input().split('-')
table = input().split('-')

piles = {'3':4, '4':4, '5':4, '6':4, '7':4, '8':4, '9':4, '10':4, 'J':4, 'Q':4, 'K':4, 'A':4}
for card in mines:
    piles[card] -= 1
for card in table:
    piles[card] -= 1

max_length = 0
left, right = 0, 0
start, end = 0, 0
while right < len(piles):
    if list(piles.values())[right] > 0:
        right += 1
    else:
        if right - left >= max_length:
            max_length = right - left
            start, end = left, right - 1
        right += 1
        left = right

# the last segment
if right - left >= max_length:
    max_length = right - left
    start, end = left, right - 1

cards = list(piles.keys())
if max_length < 5:
    print('NO-CHAIN')
else:
    print('-'.join(cards[start:end+1]))