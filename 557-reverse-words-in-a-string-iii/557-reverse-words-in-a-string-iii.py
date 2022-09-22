class Solution:
    def reverseWords(self, s: str) -> str:
        if(len(s)==1):
            return s
        return ' '.join(s.split()[::-1])[::-1]
        