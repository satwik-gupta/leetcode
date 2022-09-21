class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        sum1=0
        for i in nums:
            if(i%2==0):
                sum1+=i
        for i in range(len(queries)):
            index=queries[i][1]
            if(nums[index]%2==0):
                sum1-=nums[index]
            nums[index]=nums[index]+queries[i][0]
            if(nums[index]%2==0):
                sum1+=nums[index]
            ans.append(sum1)
        return ans