class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        a=0
        for i in range(len(nums)-1):
            if a==nums[i]:
                a+=1
            else:
                return a
        if a in nums:
            return a+1
        return a