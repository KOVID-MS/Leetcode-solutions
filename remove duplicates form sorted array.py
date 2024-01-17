class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums2 = []
        for i in range(len(nums)):
            if nums[i] not in nums2:
                nums2.append(nums[i])

        for i in range(len(nums)):
            if i < len(nums2):
                nums[i] = nums2[i]
            else:
                nums[i] = '_'
        count = len(nums2)

        return count
