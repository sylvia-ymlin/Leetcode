# Determine best upgrade time window based on average hourly traffic in past week

# Total user traffic in time window cannot exceed given threshold
# Time window must be continuous x hours. Largest x is best upgrade window. x <= 7 * 24 = 168 hours
# Time window can cross cycle, e.g. from current 167th hour to 166th hour of next cycle
# If multiple best windows exist, return smallest start index

# Traffic is consistent across cycles
# So extend array to double size, 336 hours -> Entire cycle not exceeding 168 hours
# Use sliding window, time complexity O(n)

threshold = int(input())
accesses = list(map(int, input().split()))

left = 0
right = 0

max_width = -1
result_left = -1
sum = 0
while left < 168: # Max window 168? Max start?
    # Basis is average traffic... wait, problem says "cumulative user traffic"? "Average hourly traffic" is input?
    # "Total user traffic in time window cannot exceed threshold". So likely sum.
    sum += accesses[right % len(accesses)]
    width = right - left + 1
    if sum <= threshold:
        right += 1
    else:
        if max_width < width - 1:
            max_width = width - 1
            result_left = left
        # Shrink window until condition met
        while left < right and left < 168:
            sum -= accesses[left]
            left += 1
            width -= 1
            if sum <= threshold:
                break
        right += 1


print(result_left, result_left + max_width - 1)
