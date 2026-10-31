class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        li=[nums[0],max(nums[1],nums[0])]

        for i in range(2,len(nums)):
            li.append(max([li[i-2]+nums[i],li[i-1]]))
        return li[-1]
