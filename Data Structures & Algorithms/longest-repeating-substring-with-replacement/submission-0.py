class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        di={}
        l=0
        ans=0
        for i in range(len(s)):
            if s[i] not in di:
                di[s[i]]=1
            else:
                di[s[i]]+=1

            replace= (i-l+1)-max(di.values())
            
            # in the window - the maximum letter

            if replace>k:
                di[s[l]]-=1
                l+=1
            ans=max(ans, i-l+1)
        return ans
            


            

            
        