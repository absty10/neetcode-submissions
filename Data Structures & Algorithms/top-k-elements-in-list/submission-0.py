class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap={}
        for i in nums:
            if i in hashMap:
                hashMap[i]+=1
            else: hashMap[i]=1
        hashMap=sorted(hashMap,key=hashMap.get,reverse=True)

        return hashMap[:k]