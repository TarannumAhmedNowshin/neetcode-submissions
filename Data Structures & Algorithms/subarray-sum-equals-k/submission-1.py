class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum=0
        count=0
        di={0:1}
        for i in nums:
            current_sum+=i
            need=current_sum-k 
            if need in di:
                count+=di[need]
            di[current_sum]=di.get(current_sum, 0) + 1
    


        return count
        
                    



                    
