class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s=[]
        x=set(arr)
        for i in x:
            s.append(arr.count(i))
        s.sort()
        for i in range(1,len(s)):
            if(s[i]==s[i-1]):
                return False
        return True