class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=len(s)
        n=len(p)
        dp=[[False]*(n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if(i==0 and j==0):
                    dp[i][j]=True
                elif(j==0):
                    dp[i][j]=False
                elif(i==0):
                    if(p[j-1]=='*'):
                        dp[i][j]=dp[i][j-1]
                    else:
                        dp[i][j]=False
                
                elif(s[i-1]==p[j-1] or p[j-1]=='?'):
                    dp[i][j]=dp[i-1][j-1]
                    
                elif(p[j-1]=='*'):
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j]=False
        return dp[m][n]