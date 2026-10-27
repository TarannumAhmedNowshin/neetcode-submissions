class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen={}
        for i, num in enumerate(nums):
            less= target- num
            if less in seen:
                
                return [seen[less],i]
            seen[num]=i
        return []
            



        
        


