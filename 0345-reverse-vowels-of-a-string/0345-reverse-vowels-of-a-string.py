class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        arr=list(s)
        a=""
        i=0
        j=len(s)-1
        while(i<j):
            while(i<j and arr[i] not in vowels):
                i+=1
            while(i<j and arr[j] not in vowels):
                j-=1
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        return a.join(arr)