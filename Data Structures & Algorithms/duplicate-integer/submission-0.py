class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter 

        di= Counter(nums)

        if any (count>=2 for count in di.values()) :
            return True
        return False