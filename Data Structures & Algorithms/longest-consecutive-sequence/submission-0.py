class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet=set(nums)
        maxSeq=0
        for num in nums:
            if num-1 not in hashSet:
                currentNum=num
                currentStreak=1
                while currentNum + 1 in hashSet:
                    currentNum+=1
                    currentStreak+=1
                if currentStreak>maxSeq:
                    maxSeq=currentStreak
        return maxSeq