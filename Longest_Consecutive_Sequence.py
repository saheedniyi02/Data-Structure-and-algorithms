class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        
        max_seq=0
        
        for num in nums:
            if num-1 not in nums:

                seq=1
                num_=num+1
                while num_ in nums:
                    seq+=1
                    num_+=1
                max_seq=max(seq,max_seq)
        return max_seq
                
                    
                

