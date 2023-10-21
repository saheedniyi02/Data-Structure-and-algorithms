class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
                
            x=0-nums[i]
            if (i>0) and (nums[i]==nums[i-1]):
                continue 
            j=i+1
            k=len(nums)-1
            
            while j<k:
                #print(j,k)
                if nums[j]+nums[k]<x:
                    j+=1
                elif nums[j]+nums[k]>x:
                    k-=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while (nums[j]==nums[j-1]) and (j<k):
                        j+=1
                    while (nums[k]==nums[k+1] and (j<k)):
                        k-=1
                    
                   # k-=1
        return res
            
            
          
        
