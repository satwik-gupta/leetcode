class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        count=0
        maxdefense=0
        properties.sort(key= lambda x: (-x[0],x[1]))
        for i,j in (properties):
            if(j<maxdefense):
                count+=1
            else:
                maxdefense=max(j,maxdefense)
        return count