class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,letterindex,visited):

            if [i,j] not in visited and board[i][j] == word[letterindex]:
                visited.append([i,j])
                
                if letterindex == len(word)-1:
                    return True
                else:
                    if 0<=i+1< len(board):
                        if dfs(i+1,j,letterindex+1,visited):
                            return True
                        
                    if 0<=i-1< len(board):
                        if dfs(i-1,j,letterindex+1,visited):
                            return True
                        
                    if 0<=j+1< len(board[0]):
                        if dfs(i,j+1,letterindex+1,visited):
                            return True
                        
                    if 0<=j-1< len(board[0]):
                        if dfs(i,j-1,letterindex+1,visited):
                            return True
                        
                visited.pop()
            return False
            
                            
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if dfs(i,j,0,[]):
                    return True
        return False
            

        