def fibc(num):
        if num == 0 or num == 1:
            return num
        return fibc(num-1) + fibc(num-2) 
class Solution:
    def fib(self, n: int) -> int:
        return fibc(n)