class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr_=[(position[i],speed[i]) for i in range(len(position))]
        arr_.sort()#nlogn
        #stack=[]
        last_time=-1
        fleets=0
        
        for i in range(len(arr_)-1,-1,-1):
            time=(target-arr_[i][0])/arr_[i][1]
            if time<=last_time:
                pass
            else:
                fleets+=1
                last_time=time
        return fleets
            
