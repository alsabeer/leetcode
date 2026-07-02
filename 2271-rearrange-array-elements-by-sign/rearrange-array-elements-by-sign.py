class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        final=[]
        for i in nums:
            if i < 0 :
                n.append(i)
            else:
                p.append(i)
        for i in range(len(p)):
            final.append(p[i])
            final.append(n[i])
        return final