class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        i=0
        res=0
        
        for j in range(len(s)):
            letter =s[j]
            if letter in seen:
                if seen[letter]>=i:
                    i=seen[letter]+1
            seen[letter]=j
            res=max(res,j-i+1)
        return res
