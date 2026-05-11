class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        nums=sorted(nums)
        print(nums)
        for i in range(n):
            right=n-1
            left=i+1
            while left<right:
                if nums[i] + nums[left] + nums[right]==0:
                    currList=[]
                    currList.append(nums[i])
                    currList.append(nums[left])
                    currList.append(nums[right])
                    if currList not in res:
                        res.append(currList)
                    print(currList)
                    left+=1
                    right-=1
                elif nums[i] + nums[left] + nums[right]>0:
                    right-=1

                elif nums[i] + nums[left] + nums[right]<0:
                    left+=1

        
        return res
