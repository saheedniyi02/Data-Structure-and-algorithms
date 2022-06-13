class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashmap_s=dict()
        hashmap_t=dict()
        for i in s:
            if i in hashmap_s:
                hashmap_s[i]+=1
            else:
                hashmap_s[i]=1
                
        for j in t:
            if j in hashmap_t:
                hashmap_t[j]+=1
            else:
                hashmap_t[j]=1
                
        if hashmap_s==hashmap_t:
            return True
        return False
        
