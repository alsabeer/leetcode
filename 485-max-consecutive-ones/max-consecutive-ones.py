class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        key=0
        for i in range(len(nums)):
            if nums[i] == 1 :
                key+=1
            else:
                maxi = max(maxi,key)
                key=0
        return max(maxi,key)