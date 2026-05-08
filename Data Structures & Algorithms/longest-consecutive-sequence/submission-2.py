class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap=set(nums)
        maxSeq=0
        for num in nums:
            if num-1 not in hashMap:
                currNum=num
                lenSeq=1
                while currNum+1 in hashMap:
                    currNum+=1
                    lenSeq+=1
                if lenSeq>maxSeq :
                    maxSeq = lenSeq
        return maxSeq

