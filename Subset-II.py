from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        ans = []
        nums.sort()
        n = len(nums)
        def func(ind:int,subarr:List[int]):
            if ind == n:
                res.add(tuple(subarr[:]))
                return
            
            func(ind+1,subarr + [nums[ind]])

            func(ind+1,subarr)

        func(0,[])
        for i in res:
            ans.append(list(i))
        return ans
