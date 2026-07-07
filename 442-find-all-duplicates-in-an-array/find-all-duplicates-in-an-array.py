class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr=[]
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                arr.append(nums[i])

        return arr