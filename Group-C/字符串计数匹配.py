# 给出一个字符串，统计字符串中恰好包含 k 个字母 且 {0123456789} 至少出现一次的子串数量。

# 字符串中仅包含小写字母和数字

def is_char(c):
    return 'a' <= c <= 'z'

s = input().strip()
k = int(input().strip())

n = len(s)
res = 0
left = 0
count = 0
prex = 0 # 指向当前合法最远左边界

nums = {} # 记录数字频次, 便于通过 len(nums) 判断是否包含所有数字

for right in range(n): # 右边界逐步扩展
    char_r = s[right]

    if is_char(char_r):
        count += 1
    else:
        nums[char_r] = nums.get(char_r, 0) + 1

    if count > k: # 字母数量超出，移动左边界
        while left <= right and count > k:
            if not is_char(s[left]):
                nums[s[left]] -= 1
                if nums[s[left]] == 0:
                    del nums[s[left]]
            else:
                count -= 1
            left += 1
        prex = left
    
    if count == k and len(nums) == 10:
        # break -> 移动左边界，但是始终保证区间合法
        while left <= right and count == k and len(nums) == 10:
            if not is_char(s[left]):
                if nums[s[left]] == 1:
                    break   
                else:
                    nums[s[left]] -= 1
                    left += 1
            else:
                break
        # 仅在 left， prex， right 三者均合法时，才计数
        res += (left - prex + 1)

print(res)

