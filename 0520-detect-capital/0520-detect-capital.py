class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        x=word[1:]
        if(len(word)==1):
            return True
        if(x.islower()==True or word.isupper()==True):
            return True
        else:
            return False