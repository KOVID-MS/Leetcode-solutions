class Solution(object):
    def applyOperations(self, nums):

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = 2 * nums[i + 1]
                nums[i + 1] = 0
        count = nums.count(0)
        nums[:] = [i for i in nums if i != 0]

        for i in range(count):
            nums.append(0)

        return nums
