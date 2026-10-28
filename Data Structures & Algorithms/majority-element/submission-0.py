class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter 
        a= Counter(nums)
        n= len(nums)//2

        for num, count in a.items():
            if count>n :
                return num
            
