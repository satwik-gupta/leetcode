class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        hm=Counter(tasks)
        res=0
        for i in hm.values():
            if(i<=1):
                return -1
            else:
                res+=math.ceil(i/3)
        return res