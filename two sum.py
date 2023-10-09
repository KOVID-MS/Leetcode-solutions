class Solution(object):
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        dic = {}
        for i in range(len(nums)):
            targe = target - nums[i]
            if targe in dic:
                return [i, dic[targe]]
            else:
                dic[nums[i]] = i



