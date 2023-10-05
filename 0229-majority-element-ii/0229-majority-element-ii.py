class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element1=0
        element2=0
        c1=0
        c2=0
        n=len(nums)//3
        f1,f2=0,0
        for i in nums:
            if(element1==i):
                f1+=1
            elif(element2==i):
                f2+=1
            elif(f1==0):
                element1=i
                f1=1
            elif(f2==0):
                element2=i
                f2=1
            else:
                f1-=1
                f2-=1
            
        for i in nums:
            if(element1==i):
                c1+=1
            elif(element2==i):
                c2+=1
        if(c1>n and c2>n):
            return [element1,element2]
        if(c1>n):
            return [element1]
        elif(c2>n):
            return [element2]