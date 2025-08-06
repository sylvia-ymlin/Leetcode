# 字母异位词分组, 要求返回的词组中，每个单词由相同字母组成
from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 一个暴力的方法是，我们对每个词按字母排序，异位词排序后是相同的，这样我们采用一个 nlogn 的排序算法，对 m 个词，算法的时间复杂度就是 O(m * nlogn), 空间复杂度就是存储所有词的空间 O(m * n)
        # 我们考虑一种更快的算法，不需要排序，只需要统计词中每个字母出现的次数，对于异位词，每个字母的出现次数是相同的
        res = defaultdict(list) # 使用 defaultdict 来存储结果
        for word in strs:
            # 统计每个字母出现的次数，使用一个长度为 26 的数组来表示每个字母的出现次数
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            # 将计数转换为元组作为字典的键, 对应的值是所有具有相同计数的单词
            res[tuple(count)].append(word)
        
        # 结果专为列表形式返回
        return list(res.values())