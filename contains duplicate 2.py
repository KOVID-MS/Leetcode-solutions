class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        arr = {}
        for i, n in enumerate(nums):
            if nums[i] in arr and abs(i - arr[nums[i]]) <= k:
                return True
            arr[nums[i]] = i
        return False








