class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a=max(nums)
        b=set(nums)
        n=min(nums)
        arr=[]
        while n<=a:
            if n not in b:
                arr.append(n)
            n+=1
        return arr
