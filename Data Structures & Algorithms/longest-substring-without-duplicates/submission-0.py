class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_length=0
        seen=set()
        for i in range(len(s)):

            while s[i] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[i])

            max_length = max(max_length, i - l + 1)

        return max_length