class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        dic={}
        for row in grid:
            for item in row:
                if item in dic:
                    dic[item]+=1
                else:
                    dic[item]=1
        missing=0
        repeated=0
        n=len(grid)*len(grid)
        for item in range(1,n+1):
            if item in dic:
                if dic[item]==2:
                    repeated=item
            else:
                missing=item
                
        return [repeated,missing]

         