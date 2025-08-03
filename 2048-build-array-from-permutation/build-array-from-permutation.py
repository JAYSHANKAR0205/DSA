class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            if nums[nums[i]] in nums:
                ans.append(nums[nums[i]])
        return ans
                
                


        