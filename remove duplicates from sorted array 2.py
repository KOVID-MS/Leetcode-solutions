from collections import Counter
class Solution(object):
    def removeDuplicates(self, nums):
        dic = dict(Counter(nums))
        for key,value in dic.items():
            if value > 2:
                for i in range(value - 2):
                    nums.remove(key)
        return len(nums)