class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        openClose={")":"(","}":"{","]":"["}
        for c in s:
            if c in openClose:
                #close
                if stack and stack[-1]==openClose[c]:
                    stack.pop()
                else:           
                    return False
            else:
                #add to my stack
                stack.append(c)
        if len(stack)==0:
            return True
        else:
            return False
