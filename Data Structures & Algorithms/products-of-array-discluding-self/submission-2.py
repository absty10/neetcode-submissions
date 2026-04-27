class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left = [0]*n
        right = [0]*n
        l_mult=1
        r_mult=1

        for i in range(len(nums)):
            j=-i-1
            left[i]=l_mult
            right[j]=r_mult
            l_mult*=nums[i]
            r_mult*=nums[j]

        return [l*r for l,r in zip(left,right)]



            
