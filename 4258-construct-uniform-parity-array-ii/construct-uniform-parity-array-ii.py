class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()
        odd=False
        lowestodd=10**5 -1
        for i in range(len(nums1)):
            if(nums1[i]%2==1):
                odd=True
                lowestodd=nums1[i]
                break
        if(odd and lowestodd==nums1[0]) or not odd:
            return True
        return False