class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            ind = ((right + left) // 2)
            if target == nums[ind]:
                return ind
            elif target > nums[ind]:
                left = ind + 1
            elif target < nums[ind]:
                right = ind - 1
        return left


