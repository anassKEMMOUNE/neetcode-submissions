class Solution:
    arr = {}
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        if n in self.arr.keys() :
            return self.arr[n]
        else :
            self.arr[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.arr[n]
        