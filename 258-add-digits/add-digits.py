class Solution:
    def addDigits(self, num: int) -> int:
        def addnum(n):
            if n<10:
                return n
            sum=0
            while n>0:
                sum+=n%10
                n//=10
            
            return addnum(sum)
        return addnum(num)
                
