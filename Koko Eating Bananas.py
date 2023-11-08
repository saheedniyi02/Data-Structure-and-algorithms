class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate_hours(k):
            hours=0
            for p in piles:
                hours+=math.ceil(p/k) 
            return hours
        
        i,j=1,max(piles)
        res=0
        while i<=j:
            k=(i+j)//2
            hours=calculate_hours(k)
            #print(k,hours,i,j)
            if hours<=h:
                res=k
                j=k-1
            
            if hours>h:
                i=k+1
            
        return res
