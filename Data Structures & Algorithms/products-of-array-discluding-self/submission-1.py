class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        res=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                    if i==j:
                        pass
                    else:
                        prod*=nums[j]
            res.append(prod) 
            prod=1
        return res
                    
            
