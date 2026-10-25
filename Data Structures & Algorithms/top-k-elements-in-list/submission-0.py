class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        di={}
        ans=[]
        for i in nums:
            if i not in di:
                di[i]=1
            else:
                di[i]+=1

        a = sorted(di.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            mainans=a[i][0]
            ans.append(mainans)
            
        return ans

