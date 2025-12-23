class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 同样是一个排列问题
        # 2 - 9
        # 2: "abc"
        # 3: "def"
        # 4: "ghi"
        # 5: "jkl"
        # 6: "mno"
        # 7: "pqrs"
        # 8: "tuv"
        # 9: "wxyz"

        # 每个按键有三种（或 9 对应四种）选择

        # 数组长度可能为 0
        if len(digits) == 0:
            return []
        
        phone_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def backtrack(index=0, path=""):
            # 如果当前路径的长度等于 digits 长度，说明找到一个可行解
            if len(path) == len(digits):
                res.append(path)
                return
            
            # 取当前数字对应的字母
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                # 做选择
                path += letter

                # 递归处理下一个数字
                backtrack(index + 1, path)
                
                # 撤销选择
                path = path[:-1]
        
        res = []
        backtrack()
        return res