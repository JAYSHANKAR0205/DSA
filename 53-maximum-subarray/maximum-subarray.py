class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxm=float(-inf)
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            if sum>maxm:
                maxm=sum
            if sum<0:
                sum=0
        return maxm
        