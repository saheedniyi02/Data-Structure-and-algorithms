class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i, sum_,subset):
            if sum_==target:
                res.append(subset[:])
                return 
            if i>=len(candidates) or sum_>target:
                return 
            subset.append(candidates[i])
            dfs(i+1,sum_+candidates[i],subset)
            subset.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,sum_,subset)
        dfs(0,0,[])
        return res
        
