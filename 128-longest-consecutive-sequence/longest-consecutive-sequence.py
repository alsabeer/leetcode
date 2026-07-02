class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxi=0
        count=0
        if len(nums) == 0:
            return 0
        for i in range(len(nums)-1):
            if nums[i] == (nums[i+1]-1):
                count+=1
                maxi=max(maxi,count)
            elif nums[i] == nums[i+1] :
                continue
            else:
                maxi = max(maxi,count)
                count=0
        return maxi+1