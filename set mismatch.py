from collections import Counter
class Solution(object):
    def findErrorNums(self, nums):
        arr = []
        dic = {}
        dic = dict(Counter(nums))

        for key,value in dic.items():
            if value == 2:
                arr.append(key)
        for i in range(1,len(nums)+1):
            if i not in dic:
                arr.append(i)
        return arr