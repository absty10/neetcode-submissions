class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[0]*n
        right=[0]*n
        left_mul=1
        right_mul=1
        for i in range(n):
            j=-i-1
            left[i]=left_mul
            right[j]=right_mul
            left_mul*=nums[i]
            right_mul*=nums[j]

        return [l*r for l,r in zip(left,right)]




            
