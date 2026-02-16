# Group Anagrams, request that each word in the returned group is composed of the same letters
from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # A brute force method is to sort each word by letter, anagrams will be the same after sorting, so we use an nlogn sorting algorithm, for m words, time complexity is O(m * nlogn), space complexity is O(m * n) to store all words
        # We consider a faster algorithm, no need to sort, just count the occurrence of each letter in the word, for anagrams, the occurrence of each letter is the same
        res = defaultdict(list) # Use defaultdict to store results
        for word in strs:
            # Count the occurrence of each letter, use an array of length 26 to represent the occurrence of each letter
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            # Convert count to tuple as dictionary key, corresponding value is all words with same count
            res[tuple(count)].append(word)
        
        # Return results as a list
        return list(res.values())