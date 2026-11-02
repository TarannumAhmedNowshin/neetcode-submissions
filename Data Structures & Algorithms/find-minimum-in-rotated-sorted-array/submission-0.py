class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        
        while l<r:
            mid=(l+r)//2

            if nums[mid]<nums[r]:
                #we look at the left side to the mid 
                r=mid
                
            else:
                #we look at mid to the right side 
                l=mid+1
        return nums[l]

