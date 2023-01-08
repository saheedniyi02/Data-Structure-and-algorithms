class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    

        hashmap={}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
            hashmap[target-nums[i]]=i
            
            
"""my solution loops through the list of numbers and checks the remainder for the number in the current index to hit the target and stores it in a hashmap as a 
key with the current index as value, when we encounter any remainder stored in the hashmap in the list of numbers, we return a list with the index of the remainder 
and the target-remainder"""
