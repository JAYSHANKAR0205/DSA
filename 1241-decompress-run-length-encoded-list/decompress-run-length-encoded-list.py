class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompress_lst=[]
        for i in range(len(nums)//2):
                freq=nums[2*i]
                val=nums[2*i+1]
                decompress_lst.extend([val]*freq)
        return decompress_lst