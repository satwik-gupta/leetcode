class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix=[]
        prefix.append(0)
        p=0
        for i in range(len(travel)):
            p+=travel[i]
            prefix.append(p)
        g=0
        p=0
        m=0
        gc=0
        np,ng,nm=0,0,0
        for i in garbage:
            np+=i.count('P')
            ng+=i.count('G')
            nm+=i.count('M')
        for i in range(len(garbage)-1,-1,-1):
            if('G' in garbage[i]):
                g=i
                break
            else:
                g=0
        for i in range(len(garbage)-1,-1,-1):
            if('M' in garbage[i]):
                m=i
                break
            else:
                m=0
        for i in range(len(garbage)-1,-1,-1):
            if('P' in garbage[i]):
                p=i
                break
            else:
                p=0
        gc=prefix[g]+ng+prefix[m]+nm+prefix[p]+np
        return gc