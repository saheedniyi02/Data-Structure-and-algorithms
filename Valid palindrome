class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove all non alphanumeric
        new_s=""
        for letter in s:
            if letter.isalnum():
                new_s+=letter.lower()
        for i in range(len(new_s)):
            if new_s[i]!=new_s[len(new_s)-(1+i)]:
                return False
            
        return True
