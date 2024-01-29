class Solution(object):
    def moveZeroes(self, nums):
        count = nums.count(0)
        nums[:] = [i for i in nums if i != 0]
        for i in range(count):
            nums.append(0)

        return nums