class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans=[]
        from collections import Counter
        di= Counter()

        for i in words2:
            a=Counter(i)
            di=di| a

        for i in words1:
            a=Counter(i)
            if a >=di:
                ans.append(i)
        return ans

        

                
               



            

        