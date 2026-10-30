class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums=sorted(nums)
        ans=len(nums)

        for i, num in enumerate(nums):
            if i!=num:
                ans=i
                break
        return ans


