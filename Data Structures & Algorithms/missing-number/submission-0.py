class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        total=sum(nums)

        expsum= (len(nums)*(len(nums)+1))/2

        miss= expsum-total


        return int(miss)

