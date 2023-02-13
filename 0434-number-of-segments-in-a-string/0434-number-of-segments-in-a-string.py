class Solution:
    def countSegments(self, s: str) -> int:
        ignore="!@#$%^&*()_+-=',.: "
        c=0
        for i in list(s.split()):
            if(s not in ignore):
                c+=1
        return c