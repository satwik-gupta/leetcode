class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a=set(word1)
        b=set(word2)
        l1=[]
        l2=[]
        for i in a:
            l1.append(word1.count(i))
        for i in b:
            l2.append(word2.count(i))
        if(sorted(l1)==sorted(l2) and sorted(a)==sorted(b)):
            return True
        else:
            return False