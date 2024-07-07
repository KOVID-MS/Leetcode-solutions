def threeSum(self, nums):
    res = []
    nums.sort()
    if len(nums) < 3:
        return res

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] < 0:
                l += 1
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res