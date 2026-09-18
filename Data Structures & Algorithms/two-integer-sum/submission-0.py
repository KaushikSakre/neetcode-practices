class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps={}

        for i,num in enumerate(nums):
            value = target-num
            if value in maps:
                return [maps[value],i]

            maps[num]=i            
        