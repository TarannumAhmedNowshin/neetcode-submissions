class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l=0
    
        r=len(numbers)-1
        ans=[]
        while l<r:
            need=numbers[l]+numbers[r]
            if need==target:
                ans.append(l+1)
                ans.append(r+1)
                break

            elif need > target:
                r-=1
            else:
                l+=1
        return ans

        return ans