class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currentSum=0
        count=0
        hashmap={0:1}
        for i in range(len(nums)):
            currentSum+=nums[i]
            if(currentSum-k in hashmap):
                count+=hashmap[currentSum - k]
            if currentSum not in hashmap:
                hashmap[currentSum]=1
            else:
                hashmap[currentSum]+=1
        return count