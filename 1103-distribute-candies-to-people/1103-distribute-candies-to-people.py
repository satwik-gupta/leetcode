class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res=[0]*num_people
        c=1
        x=1
        while(candies>0):
            if(candies<x):
                res[c-1]+=(candies)
                candies-=candies
            else:
                res[c-1]+=(x)
                candies-=x
            c+=1
            x+=1
            if(c>num_people):
                c=c%num_people
        return res