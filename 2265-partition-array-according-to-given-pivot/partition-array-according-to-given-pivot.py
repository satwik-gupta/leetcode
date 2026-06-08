class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        more=[]
        equal=[]

        for i in range(len(nums)):
            if nums[i]<pivot:
                less.append(nums[i])
            elif(nums[i]==pivot):
                equal.append(nums[i])
            else:
                more.append(nums[i])

        res=less+equal+more
        return res