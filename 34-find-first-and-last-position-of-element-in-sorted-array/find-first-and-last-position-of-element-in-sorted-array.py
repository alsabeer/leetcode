class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=-1
        u=len(nums)
        f,la=0,len(nums)-1
        while(f<=la):
            mid=(f+la)//2
            if (nums[mid]>=target):
                l=mid
                la=mid-1
            else:
                f=mid+1
        if l == -1 or nums[l] != target:
            return [-1, -1]
        f,la=0,len(nums)-1
        while(f<=la):
            mid=(f+la)//2
            if (nums[mid]>target):
                u=mid
                la=mid-1
            else:
                f=mid+1
        return [l,u-1]