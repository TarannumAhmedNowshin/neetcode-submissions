class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        nums=sorted(nums)
        count=1
        new_count=1

        if nums==[]:
            return 0

        if len(nums)==1:
            return count

        for i in range(1,len(nums)):
            
        
            if nums[i]==nums[i-1]+1 :
                new_count+=1
            else:
                new_count=1
            count=max(count,new_count)
        return count


