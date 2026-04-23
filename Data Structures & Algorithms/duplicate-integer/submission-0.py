class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDuplicate=set(nums)
        if len(nums) != len(noDuplicate):
            return True
        else: return False
