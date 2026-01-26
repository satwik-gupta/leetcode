class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        l=0
        max_length=1
        current_length=1
        hashmap={}
        hashmap[s[l]]=1
        for r in range(1,len(s)):
            if(s[r] not in hashmap):
                hashmap[s[r]]=1
                current_length+=1
            else:
                while s[r] in hashmap and l<r:
                    del hashmap[s[l]]
                    l+=1
                    current_length-=1
                hashmap[s[r]]=1
                current_length+=1
            
            max_length=max(max_length,current_length)
        return max_length