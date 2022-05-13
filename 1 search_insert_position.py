class Solution:
    def binary_search(self,array, start, end,element):
        if element<array[0]:
            return 0


        elif element>array[-1]:
            return len(array)

 

        if start > end:

            return start




        mid = (start + end) // 2

        if element == array[mid]:

            return mid

    

        if element < array[mid]:


            return self.binary_search(array,  start, mid-1,element)

        else:


            return self.binary_search(array, mid+1, end,element)
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums,0,len(nums)-1,target)
