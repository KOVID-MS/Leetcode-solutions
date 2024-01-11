from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        self.nums = nums
        dictionary = dict(Counter(nums))
        for key, value in dictionary.items():
            if value == 1:
                return key
