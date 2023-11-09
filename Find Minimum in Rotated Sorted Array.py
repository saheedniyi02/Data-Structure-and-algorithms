class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        res=nums[0]
        while i<=j:
            mid=(i+j)//2            
            res=min(res,nums[mid])
            if nums[j]>nums[i]:
                res=min(res,nums[i])
                break
            
            #if start is greater than mid, search the left side
            if nums[i]>nums[mid]: 
                j=mid-1
            else:
                i=mid+1
        return res
        
