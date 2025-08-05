class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lst=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            if nums[i]==target:
                lst.append(i)
        return lst
            
        