class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        m=n
        while True:
            temp=m
            p=1
            while temp != 0:
                p=p*(temp%10)
                temp = temp//10
            if p % t == 0:
                return m
            else:
                m=m+1