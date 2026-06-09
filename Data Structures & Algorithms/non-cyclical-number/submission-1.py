class Solution:
    def sumsquare(self,n) :
        return  sum([int(i)**2 for i in list(str(n))])
    def isHappy(self, n: int) -> bool:
        dicto = {i:0 for i in range(1001)}
        while dicto[n] == 0 :
            dicto[n] = 1
            n = self.sumsquare(n)
        if n == 1 : 
            return True
        else :
            return False
        