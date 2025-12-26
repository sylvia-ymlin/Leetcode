# 要求按照 高，矮，高，矮 的顺序排列一组人的身高数据
# 输出排列后的身高数据
# 相邻可以相等

# 遍历每个元素，判断当前元素的索引是奇数还是偶数，奇数要求不小于后一个元素，偶数要求不大于后一个元素
# 因为每一个元素遍历到时，一定已经和前一个元素满足要求了
# 要求元素移动距离最小，因此每次只和相邻元素交换位置

try:
    nums = list(map(int, input().split()))
except: # 输入不是 int
    print([])
    exit()

if nums[0] < nums[1]:
    nums[0], nums[1] = nums[1], nums[0]

for i in range(1, len(nums)-1):
    if i % 2 == 0:
        if nums[i] < nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
    else:
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]

print(' '.join(map(str, nums)))