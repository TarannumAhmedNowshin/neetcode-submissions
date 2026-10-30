class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=len(nums)
        nums=set(nums)
        ans=[]
        for i in range(l+1):
            if i==0:
                continue
            else:
                if i not in nums:
                    ans.append(i)

        return ans
