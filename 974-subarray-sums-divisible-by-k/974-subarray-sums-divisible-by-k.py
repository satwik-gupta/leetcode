class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        i=0
        st={0:1}
        ans=0
        if(len(nums)==1 and nums[0]%k!=0):
            return 0
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]
        for i in range(len(nums)):
            rem=nums[i]%k
            if rem in st:
                ans+=st[rem]
            if rem not in st:
                st[rem]=1
            else:
                st[rem]+=1
        return ans