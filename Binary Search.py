class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(low,high):
            #print(low,high)
            mid=(low+high)//2
            #print(low,high,nums[mid])
            if low>high:
                return -1
            
            if nums[mid]==target:
                return mid
            
            if nums[mid]>target:
                return binary_search(low,mid-1)
            else:
                return binary_search(mid+1, high)
        return binary_search(0, len(nums)-1)
           
        
