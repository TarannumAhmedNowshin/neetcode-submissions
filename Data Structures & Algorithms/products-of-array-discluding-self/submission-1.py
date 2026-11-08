class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        li=[]
        left_prod=1
        right_prod=1
        
        for i in range(len(nums)):
            li.append(left_prod)
            left_prod*=nums[i]
        for i in range( len(nums)-1, -1,-1):
            li[i]=li[i]* right_prod
            right_prod*=nums[i]
        return li
            


            
