class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans=0
        from collections import defaultdict

        freq= defaultdict(int)

        for i in s:
            freq[i]+=1

        for x in freq.values():
            if x%2==0: # 2,4 even so just directly add them
                ans+=x
            else:
                ans+=x-1 # 1,3,5 odd so just deduce the odd values and add the pair that exists

        if ans<len(s):
            ans+=1
        return ans

            


