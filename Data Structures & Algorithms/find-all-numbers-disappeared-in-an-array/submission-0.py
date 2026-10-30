class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)+1):
            if i==0:
                continue
            else:
                if i not in nums:
                    ans.append(i)

        return ans
