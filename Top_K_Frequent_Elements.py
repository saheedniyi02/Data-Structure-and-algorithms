class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #let's use a bucket sort

        #IDEA: create  a list of list with the position being the value count and the values in the list being the nums with that index as occurence.
        counts={} #to store the num and the count
        freq=[[] for i in range(len(nums)+1)]
        
        for num in nums:
            #save the counts of each number
            counts[num]=1+counts.get(num,0)
            
        for num, count in counts.items():
            freq[count].append(num)
            
        res=[]
        
        for i in range(len(nums),0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
