class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        maximumScore = 0
        tokens.sort()    

        while(tokens):
            if(power>=tokens[0]):
                minimum = tokens.pop(0)
                power -= minimum
                score += 1
                if(score>maximumScore):
                    maximumScore = score
            else:
                if(score>=1):
                    maximum = tokens.pop()
                    power += maximum
                    score -= 1
                else:
                    break
            
        return(maximumScore)