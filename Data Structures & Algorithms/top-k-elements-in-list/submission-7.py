class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap={}
        for num in nums:
            if num in hashMap:
                hashMap[num]+=1
            else:
                hashMap[num]=1
        buckets=[[] for i in range(0,len(nums)+1)]
        for i in hashMap:
            buckets[hashMap[i]].append(i)
        res=[]
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res