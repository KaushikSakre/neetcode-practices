class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l,r,count = 0,0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                r+1
                l=r
            elif nums[i]==1:
                count = max(count,r-l+1)
                r+=1

        return count
        