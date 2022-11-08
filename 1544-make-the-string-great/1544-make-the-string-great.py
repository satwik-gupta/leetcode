class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        stack.append(s[0])
        for i in range(1,len(s)):
            if(len(stack)==0):
                stack.append(s[i])
            else:
                if(stack[-1].islower() and s[i].isupper()):
                    if(stack[-1]==s[i].lower()):
                        stack.pop()
                    else:
                        stack.append(s[i])
                elif(stack[-1].isupper() and s[i].islower()):
                    if(stack[-1]==s[i].upper()):
                        stack.pop()
                    else:
                        stack.append(s[i])
                else:
                    stack.append(s[i])
        return "".join(stack)