class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic={}
        for i in range(len(arr)):
            if arr[i] in dic:
                dic[arr[i]]+=1
            else:
                dic[arr[i]]=1
        count=set()
        for num in dic.values():
            if num in count:
                return False
            count.add(num)
        return True
            
