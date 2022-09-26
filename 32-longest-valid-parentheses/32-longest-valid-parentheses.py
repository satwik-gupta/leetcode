class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[(0,-1)]
        
        if(len(s)==0 or len(s)==1):
            return 0
        else:
            count=0
            for i in range(len(s)):
                if(s[i]==')' and stack[-1][0]=='('):
                    stack.pop()
                    count=max(count,i-stack[-1][1])
                else:
                    stack.append((s[i],i))
            return count