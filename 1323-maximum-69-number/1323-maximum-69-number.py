class Solution:
    def maximum69Number (self, num: int) -> int:
        num=list(str(num))
        for i in range(len(num)):
            if(num[i]!='9'):
                num[i]='9'
                break
            else:
                continue
        return "".join(num)