class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set(nums)
        count=0
        for num in hashset:
            if num-1 not in hashset:
                curr_count=1
                while num+1 in hashset:
                    num+=1
                    curr_count+=1
                count=max(count,curr_count)
        return count