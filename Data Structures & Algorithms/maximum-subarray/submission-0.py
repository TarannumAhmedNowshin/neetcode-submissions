class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current_sum=0
        maxx=nums[0]

        for i in range(len(nums)):
            current_sum+=nums[i]

            maxx= max(current_sum, maxx)

            if current_sum<0:
                current_sum=0
        return maxx