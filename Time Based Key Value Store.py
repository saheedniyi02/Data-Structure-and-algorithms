class TimeMap:


    def __init__(self):
        self.map=dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((value,timestamp))
        else:
            self.map[key]=[(value,timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        
        res=""
        values=self.map.get(key,[])
        l,r=0,len(values)-1
        
        while l<=r:
            
            m=(l+r)//2
            if values[m][1]==timestamp:
                return values[m][0]
            if values[m][1]<=timestamp:
                res=values[m][0]
                l=m+1
            else:
                r=m-1
            
        return res
                    
                    
                    
