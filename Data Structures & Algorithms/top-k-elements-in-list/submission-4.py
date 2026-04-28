class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap={}
        res=[]
        for i in nums:
            if i in hashMap:
                hashMap[i]+=1
            else: hashMap[i]=1

        print(hashMap)
        hashMap=sorted(hashMap, key=hashMap.get, reverse=True)

        print(hashMap)

        
        for i in range(k):
            res.append(hashMap[i])

        print(res)
        return res