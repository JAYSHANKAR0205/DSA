class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary={}
        count=0
        for i in nums:
            if i in dictionary:
                dictionary[i]+=1
            else:
                dictionary[i]=1

        for i in dictionary:
            if dictionary[i]>len(nums)//2:
                return i
        


        