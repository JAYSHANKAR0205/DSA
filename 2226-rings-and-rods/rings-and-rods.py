class Solution:
    def countPoints(self, rings: str) -> int:
        red=[0]*10
        green=[0]*10
        blue=[0]*10
        for i in range(0,len(rings),2):
            color=(rings[i])
            rod=int(rings[i+1])

            if color=='R':
                red[rod]=1
            elif color=='G':
                green[rod]=1
            else:
                blue[rod]=1
        
        count=0
        for i in range(10):
            if (red[i]==1 and blue[i]==1 and green[i]==1):
                count+=1
        return count




        