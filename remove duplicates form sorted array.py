class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        nums2 = []
        for num in nums:
            if num not in nums2:
                nums2.append(num)
        nums[:] = nums2
        return len(nums)
