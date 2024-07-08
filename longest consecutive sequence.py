class Solution(object):
    def longestConsecutive(self, nums):
        numbers = set(nums)
        length = 0

        for num in numbers:
            if num-1 not in numbers:
                l = 1
                dup = num

                while dup + 1 in numbers:
                    dup += 1
                    l += 1

                length = max(length,l)
        return length