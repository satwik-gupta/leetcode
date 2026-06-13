class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=""
        for i in range(len(words)):
            word=words[i]
            currsum=0
            for j in range(len(word)):
                currsum+=weights[ord(word[j])-97]
            conweight=currsum%26
            ans+=str(chr(122-conweight))
        return ans