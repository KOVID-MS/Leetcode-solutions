def summaryRanges(self, nums):
    res = []
    if nums == []:
        return res
    first = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            continue
        if first == nums[i - 1]:
            res.append(str(first))
        else:
            res.append(str(first) + '->' + str(nums[i - 1]))
        first = nums[i]
    if first == nums[-1]:
        res.append(str(first))
    else:
        res.append(str(first) + '->' + str(nums[-1]))
    return res