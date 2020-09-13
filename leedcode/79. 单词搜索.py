
class Solution:
    board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    word = "ABCCED"
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x,y,k):
            if board[x][y]!= word[k]:
                return False
            if k == len(word)-1:
                return True

            result = False
            for x1,y1 in keep:
                x2 = x+x1
                y2 = y+y1
                if 0<=x2<len(board) and 0<=y2<len(board[0]):
                    if dfs(x2,y2,k+1):
                        result = True
                        break
            return result
        keep = [[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                    if dfs(i,j,0):
                        return True
        return False