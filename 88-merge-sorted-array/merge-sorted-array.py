class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Brute Force Ever 
        dic={}
        lst=[]
        for num in nums1[:m]:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        for num in nums2[:n]:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        for item,count in dic.items():
            lst.extend([item]*count)
        lst.sort()
        for i in range(len(lst)):
            nums1[i]=lst[i]