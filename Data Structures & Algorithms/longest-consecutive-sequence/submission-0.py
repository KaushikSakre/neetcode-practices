class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for n in s:
            if n-1 not in s:
                length = 1
                curr=n
                while curr+1 in s:
                    curr+=1
                    length+=1

                longest = max(longest,length)

        return longest