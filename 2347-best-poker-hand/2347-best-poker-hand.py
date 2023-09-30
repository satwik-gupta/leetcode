class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        countsuit=[0]*len(suits)
        countranks=[0]*13
        for i in range(5):
            countsuit[ord(suits[i])-97]+=1
            countranks[ranks[i]-1]+=1
        x=max(countsuit)
        y=max(countranks)
        if(x==5):
            return "Flush"
        elif(y>=3):
            return "Three of a Kind"
        elif(y==2):
            return "Pair"
        else:
            return "High Card"