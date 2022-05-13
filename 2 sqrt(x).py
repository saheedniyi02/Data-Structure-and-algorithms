class Solution:
    
    def binary_search(self,start,end, element):
        if start >end:
            return end
        
        mid=(start+end)//2
        if element==mid*mid:
            return mid
        
        elif element<mid*mid:
            return self.binary_search(start,mid-1,element)
        else:
            return self.binary_search( mid+1,end, element)
    def mySqrt(self, x: int) -> int:
        if x in [0,1]:
            return x
        array=range(1,x)
        start=1
        end=x//2
        return self.binary_search(start,end,x)
       
        
        
        

        