class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        di={}
        ans=0
    

        for i in range(len(s)):
            if s[i] not in di:
                di[s[i]]=i
            else:

                if di[s[i]] >= l:
                    l = di[s[i]] + 1
                di[s[i]]=i
            ans=max(i-l+1,ans)
        return ans

            


        
