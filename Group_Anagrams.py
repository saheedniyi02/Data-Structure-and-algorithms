class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        
        """#solution 1
        for word in strs:
            sorted_word=tuple(sorted(word))
            if sorted_word in ans:
                ans[sorted_word].append(word)
            else:
                ans[sorted_word]=[word]
            #print(ans)
        return ans.values()"""
            
        
        #soluion 2
        ans=collections.defaultdict(list)
        for word in strs:
            count=[0]*26
            
            for c in word:
                count[ord(c)-ord("a")]+=1
                
            ans[tuple(count)].append(word)
            
        return ans.values()
