class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in range(0,len(nums),2):
            while nums[i]>0:
                lst.append(nums[i+1])
                nums[i]-=1
        return lst