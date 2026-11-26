class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        ans=0
        inside=set()
        for i in range(len(s)):
            while s[i] in inside:
                inside.remove(s[start])
                start+=1
            inside.add(s[i])
            ans=max(ans,len(inside))
        return ans


            


        
