class Solution(object):
    def searchRange(self, nums, target):
        self.nums = nums
        self.target = target
        if len(nums) == 0:
            return [-1,-1]

        if target not in nums:
            return [-1,-1]

        for i in range(len(nums)):
            if nums[i] == target:
                return [i,len(nums)-list(reversed(nums)).index(nums[i])-1]
