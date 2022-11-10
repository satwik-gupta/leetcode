class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        stack.append(s[0])
        for i in range(1,len(s)):
            if(len(stack)==0):
                stack.append(s[i])
            else:
                if(s[i]==stack[-1]):
                    stack.pop()
                else:
                    stack.append(s[i])
        return "".join(stack)