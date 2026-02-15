class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums=[(nums[i],i) for i in range(len(nums))]
        nums.sort(reverse=True)
        if nums[0][0]!=nums[1][0] and nums[0][0]>=2*nums[1][0]:
            return nums[0][1]
        else:
            return -1