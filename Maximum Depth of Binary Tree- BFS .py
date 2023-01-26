class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #bread first search 
        
        if not root:
            return 0
        level=0
        q=deque([root])
        
        while q:
            for i in range(len(q)):
                node=q.popleft()
                
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            level+=1
        return level
                        
