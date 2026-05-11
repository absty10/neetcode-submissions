class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenNum = len(nums)
        left=[0]*lenNum
        right=[0]*lenNum
        left_mul=1
        right_mul=1

        for i in range(lenNum):
            left[i]=left_mul
            left_mul*=nums[i]
            right[lenNum-1-i]= right_mul
            right_mul*=nums[lenNum-1-i]

        return [left*right for left,right in zip(left,right)]



            
