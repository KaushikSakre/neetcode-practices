class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1

        buckets=[[]for _ in range(len(nums)+1)]

        for num,cnt in count.items():
            buckets[cnt].append(num)

        res=[]
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res


