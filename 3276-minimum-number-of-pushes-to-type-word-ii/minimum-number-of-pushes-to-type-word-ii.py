class Solution:
    def minimumPushes(self, word: str) -> int:
        count={}
        ans=0
        for i in word:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        sorted_values = sorted(count.values(), reverse=True)
        for i in range(len(sorted_values)):
            counter=math.ceil((i+1)/8)
            ans+=counter*sorted_values[i]
        return ans
