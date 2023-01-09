class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            #sorted
            if nums[l]<=nums[mid]:
                #nums[7,8,9,10,1,2], target=10
                if target>nums[mid]:
                    l=mid+1
                #[7,8,9,10,1,2]target=1
                elif target<nums[l]:
                    l=mid+1
                #[7,8,9,10,1,2] target=8
                else:
                    r=mid-1
            #unsorted [11,12,1,2,3,4,5,..]
 
            else:
        
                #[11,12,1,2,3,4,5,6] target=1
                if target<nums[mid]:
                    r=mid-1
                #[11,12,1,2,3,4,5,6] target=11
                elif target>nums[r]:
                    r=mid-1
                #[11,12,1,2,4,4,5,6] target=5
                else:
                    l=mid+1
        return -1
                  
               
                
               
              
                
