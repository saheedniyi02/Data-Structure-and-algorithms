class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary_search row
        i,j=0,len(matrix)-1
        while i<=j:
            mid=(i+j)//2
            if matrix[mid][0]<=target  and matrix[mid][-1]>=target:
                break
            if matrix[mid][0]>target:
                j=mid-1
            elif matrix[mid][-1]<target:
                i=mid+1
        if i>j:
            return False
        #print(mid)
        
        x,y=0,len(matrix[mid])
        
        while x<=y:
            #print(x,y)
            mid_col=(x+y)//2
            if matrix[mid][mid_col]==target:
                return True 
            if matrix[mid][mid_col]>target:
                y=mid_col-1
            else:
                x=mid_col+1
        return False
