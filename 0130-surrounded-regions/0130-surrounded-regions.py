class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        coordinates=[]
        for k in range(max(m,n)):
            edges=(0,k),(k,0),(m-1,k),(k,n-1)
            for edge in edges:
                if(edge not in coordinates and edge[0]<m and edge[1]<n):
                    coordinates.append(edge)
        while coordinates:
            i,j=coordinates.pop()
            if(0<=i<m and 0<=j<n and board[i][j]=='O'):
                board[i][j]='#'
                coordinates+=(i,j+1),(i,j-1),(i+1,j),(i-1,j)
        for i in range(m):
            for j in range(n):
                if(board[i][j]=='#'):
                    board[i][j]='O'
                else:
                    board[i][j]='X'
        return board