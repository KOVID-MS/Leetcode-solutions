class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        self.val = val
        nums2 = []
        i = 0
        while i <= len(nums) - 1:
            if nums[i] != val:
                nums2.append(nums[i])
                i += 1
            else:
                i += 1

        for i in range(len(nums)):
            if i < len(nums2):
                nums[i] = nums2[i]
            else:
                nums[i] = '_'

        return len(nums2)


