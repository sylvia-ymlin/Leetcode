# Decode String
# Process content inside brackets first -> Recursion -> Stack
# Numbers and "[" always appear together
# Number range [1, 300] -> could be multi-digit -> need to concatenate to number

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_str = '' # Maintain currently decoded string
        for char in s:
            # print("cur_str:", cur_str)
            # print("cur_num:", cur_num)
            # print("stack:", stack)
            # print("\n")
            if char.isdigit():
                cur_num = cur_num * 10 + int(char)
            elif char == '[':
                # Previous string pushed onto stack, current repetition count pushed onto stack
                stack.append((cur_str, cur_num))
                cur_str = ''
                cur_num = 0
            elif char == ']':
                last_str, num = stack.pop()
                # One decoding completed
                cur_str = last_str + num * cur_str
            else:
                cur_str += char
        
        return cur_str

test = Solution()
print(test.decodeString("3[a]2[bc]"))