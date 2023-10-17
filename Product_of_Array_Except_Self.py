class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        prefix=nums[0]
        # [1,2,3,4]
        for i in range(1,len(nums)):
            res[i]=prefix
            prefix=nums[i]*prefix
        postfix=nums[-1]
        for i in range(len(nums)-2,-1,-1):            
            res[i]=res[i]*postfix 
            print(i, postfix)
            postfix=postfix*nums[i]
        return res
        
