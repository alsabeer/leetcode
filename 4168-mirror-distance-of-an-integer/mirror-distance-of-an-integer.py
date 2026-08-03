class Solution:
    def mirrorDistance(self, n: int) -> int:
        a = n
        k = 0
        while a != 0:
            digit = a % 10
            k = k * 10 + digit
            a = a // 10
        return abs(k-n)