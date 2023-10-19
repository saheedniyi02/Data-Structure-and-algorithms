class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        i=0
        j=len(s)-1
        while (i<j):

            while not self.alphanum(s[j]) and i<j :
                j-=1
            while not self.alphanum(s[i]) and i<j:
                i+=1
            print(s[j],s[i])
            if s[j]!=s[i]:
                return False
            j-=1
            i+=1
        return True
    def alphanum(self,c):
        return (ord("a")<=ord(c)<=ord("z")) or (ord("0")<=ord(c)<=ord("9")) 
   
        
            
