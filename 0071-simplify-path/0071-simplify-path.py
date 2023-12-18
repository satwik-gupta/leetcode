class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        buff=path.split("/")
        for i in buff:
            if(len(stack) and i==".."):
                stack.pop()
            if(i not in [".","",".."]):
                stack.append(i)
        return '/'+"/".join(stack)