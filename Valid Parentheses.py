class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen={")":"(","]":"[","}":"{"}
        stack=[]
        if len(s) % 2 == 1:
            #if the length isn't even 
            return False

        for c in s:
            #if it's a closing paranthesis
            if c in closeToOpen:
                #if there is an element in the stack and the last element is the opening parentheses of the current closing parentheses 
                if stack and stack[-1]==closeToOpen[c]:
                    stack.pop()
                else:
                    #if the last opening parentheses isn't the opening parentheses of the current closing parentheses and our stack is empty then it isn't valid 
                    return False 
            #if it's a closing parentheses 
            else:
                stack.append(c)
        return True if not stack else False
                
                
           
        
