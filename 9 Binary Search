class Solution:
    def binary_search(self,nums,i,j,target):
        mid=(i+j)//2
        if i<=j:
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                return self.binary_search(nums,mid+1,j,target)
            else:
                return self.binary_search(nums,i,mid-1,target)
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums,0,len(nums)-1,target)
