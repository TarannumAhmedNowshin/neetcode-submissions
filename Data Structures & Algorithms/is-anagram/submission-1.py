class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        d2={}
        count=0

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1
        c=0
        for i in range(len(t)):
            if t[i] not in d2:
                d2[t[i]]=1
            else:
                d2[t[i]]+=1

        if d==d2:
            return True
        return False

        