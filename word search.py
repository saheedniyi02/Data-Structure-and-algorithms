class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path=set()
        def dfsi,r,c):
            if i==len(word):
                return True
            if r<0 or r>len(board)-1 or c<0 or c>len(board[0]) -1 or (board[r][c]!=word[i]) or ((r,c) in path):
                return False
            
            path.add((r,c))
            res= dfs(i+1,r+1,c) or dfs(i+1,r,c+1) or dfs(i+1,r-1,c) or dfs(i+1,r,c-1)
            path.remove((r,c))
            
            return res
        
        for r in range(len(board)) :
            for c in range(len(board[0])):
                if dfs(0,r,c):
                    return True
        return False
        
        
