# Defect detection and correction for center element of 3x3 matrix

# 1. Defect judgment: Absolute difference between center element and mean of surrounding 8 elements
# - diff > 50: Replace center element with round(mean)
# - 30 <= diff <= 50: Replace center element with overall mean of 3x3 matrix
# - diff < 30: No processing

# Output corrected matrix

# Total 3 lines, just calculation
matrix = []
for _ in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

center = matrix[1][1]
total = 0
for i in range(3):
    for j in range(3):
        total += matrix[i][j]

mean_neighbors = (total - center) / 8.0
diff = abs(center - mean_neighbors)

if diff > 50:
    matrix[1][1] = round(mean_neighbors)
elif 30 <= diff <= 50:
    overall_mean = total / 9.0
    matrix[1][1] = round(overall_mean)

for row in matrix:
    print(' '.join(map(str, row)))