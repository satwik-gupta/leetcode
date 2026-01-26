class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if(len(fruits))==1:
            return 1
        l=0
        hashmap={}
        count=0
        for r in range(len(fruits)):
            hashmap[fruits[r]]=hashmap.get(fruits[r],0)+1

            while(len(hashmap)>2):
                hashmap[fruits[l]]-=1
                if(hashmap[fruits[l]]==0):
                    del hashmap[fruits[l]]
                l+=1
            count=max(count,r-l+1)
        return count

                    