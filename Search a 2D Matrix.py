class Solution:
    def binary_search(self,nums, target):
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            if nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            print(nums)
            if (nums[0]<=target) and (nums[-1]>=target):
                #print(nums)
                return self.binary_search(nums, target)
           
