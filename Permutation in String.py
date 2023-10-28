class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        hash_s1,hash_s2=[0]*26,[0]*26
        for i in s1:
            hash_s1[ord(i)-ord("a")]+=1
        j=0
        
        for k in range(len(s2)):
            hash_s2[ord(s2[k])-ord("a")]+=1
            #print(s2[j:k+1])
            
            if hash_s2==hash_s1:
                return True
            
            if k+1-j==len(s1):
                hash_s2[ord(s2[j])-ord("a")]-=1
                j+=1
                
        return False
            
        
