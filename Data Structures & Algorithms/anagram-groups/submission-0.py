from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for words in strs:
            count=[0]*26
            for c in words:
                idx = ord(c)-ord('a')
                count[idx]+=1

            key = tuple(count)
            d[key].append(words)

        return list(d.values())
            
