class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        li=[]
        newli=[]
        ans=0
        if x>y:
            k=True
        else:
            k=False
        
        if k :
            first="ab"
            first_score=x
            second="ba"
            second_score=y
        else:
            first="ba"
            first_score=y
            second="ab"
            second_score=x
    
        for i in range(len(s)):
            if li==[]:
                li.append(s[i])
            else:
                if li[-1]+s[i]==first:
                    li.pop()
                    ans+=first_score
                else:
                    li.append(s[i])

        for i in li:
            if newli==[]:
                newli.append(i)
            else:
                if newli[-1]+i==second:
                    newli.pop()
                    ans+=second_score
                else:
                    newli.append(i)
        return ans



                



