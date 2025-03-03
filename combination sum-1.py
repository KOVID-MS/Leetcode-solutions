class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def recursion(ind:int, subset:List[int],target:int):
            if ind >= n or target<0:
                return

            if target == 0:
                res.append(subset[:])
                return
            
            recursion(ind,subset+[candidates[ind]],target - candidates[ind])
 
            recursion(ind+1,subset,target)
        
        recursion(0,[],target)

        return res
