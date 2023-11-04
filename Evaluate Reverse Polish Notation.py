class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
            if t=="+":
                stack.append(stack.pop()+stack.pop())
            elif t=="-":
                stack.append(-stack.pop()+stack.pop())
            elif t=="/":
                a,b=stack.pop(),stack.pop()
                stack.append(int(b/a))
            elif t=="*":
                stack.append(stack.pop()*stack.pop())
            else:
                stack.append(int(t))
        return stack[0]
        
