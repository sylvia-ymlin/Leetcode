# 字符串解码
# 先处理括号内的内容 -> 递归 -> 栈
# 数字和“["总是绑定出现
# 数字取值范围 【1， 300】 -> 可能是多位数 -> 需要拼接转数字

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_str = '' # 维护当前完成解码的字符串
        for char in s:
            # print("cur_str:", cur_str)
            # print("cur_num:", cur_num)
            # print("stack:", stack)
            # print("\n")
            if char.isdigit():
                cur_num = cur_num * 10 + int(char)
            elif char == '[':
                # 上一次的字符串入栈，本次重复次数入栈
                stack.append((cur_str, cur_num))
                cur_str = ''
                cur_num = 0
            elif char == ']':
                last_str, num = stack.pop()
                # 一个解码完成
                cur_str = last_str + num * cur_str
            else:
                cur_str += char
        
        return cur_str

test = Solution()
print(test.decodeString("3[a]2[bc]"))