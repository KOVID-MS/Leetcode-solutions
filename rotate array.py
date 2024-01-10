class Solution(object):
    def rotate(self, nums, k):
        self.k = k
        k = k % len(nums)
        arr1 = nums[-k:]
        nums[:] = arr1 + nums[:-k]
        return nums




