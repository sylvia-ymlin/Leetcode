# Given a network configuration list, each config is a string consisting of digits, '*', '?'
# Input user's IMSI, match according to rules:
# '*': 0 or more consecutive characters
# '?': Single character at odd index; index starts from 0

# Output all matching configurations, sorted lexicographically ascending. Return null if none.

# Read network configuration list
configs = input().split(',')
# Read user IMSI
imsi = input().strip()

# Check match for each config
# Dynamic programming. For '?', must match single character
# For '*', choose number of matched characters -> i.e., one '?' can use multiple times? No, that's weird translation. 
# '*' matches 0 or more characters. '?' matches single char at odd index.

def is_match(config, imsi, i, j):
    # i, j are indices for config and imsi
    if i == len(config) and j == len(imsi):
        return True
    if j == len(imsi):
        # imsi exhausted, config can only have '*' left
        return all(c == '*' for c in config[i:])
    if i == len(config): # config exhausted, imsi remains, not matched
        return False
    
    if config[i] == '*':
        # Match 0: i + 1, j unchanged
        # Match 1 or more: i unchanged, j + 1
        return is_match(config, imsi, i + 1, j) or is_match(config, imsi, i, j + 1)
    if config[i] == '?': # Can only match single character, and j must be odd index
        if j % 2 == 1:
            return is_match(config, imsi, i + 1, j + 1)
        else:
            return False
    # Normal character, must be equal
    if config[i] == imsi[j]:
        return is_match(config, imsi, i + 1, j + 1)
    else:
        return False

matched_configs = []
for config in configs:
    if is_match(config, imsi, 0, 0):
        matched_configs.append(config)

if matched_configs:
    matched_configs.sort()
    print(','.join(matched_configs))
else:
    print('null')