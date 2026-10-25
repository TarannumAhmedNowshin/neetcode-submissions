class Solution:
    def isPalindrome(self, s: str) -> bool:

        s=s.lower()

        a=""
        for i in range(len(s)):
            if s[i].isalnum()==True:
                a+=s[i]

        i=0
        j=len(a)-1

        out=True
        while i<j:
            if a[i]==a[j]:
                i+=1
                j-=1
                out= True
            else:
                out=False
                break
        return out
