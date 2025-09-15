class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        def binSearch(nums,target,start,end):
            if start<=end:
                mid=(start+end)//2
                if nums[mid]==target:
                    return mid
                if nums[mid]>target:
                    return binSearch(nums,target,start,mid-1)
                if nums[mid]<=target:
                    return binSearch(nums,target,mid+1,end)
                
            return -1
        return binSearch(nums,target,start,end)
        