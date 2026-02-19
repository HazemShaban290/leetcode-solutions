class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        
        for i in range(n-2):
            for j in range(i+1, n-1):
                x = nums[i] + nums[j]
                
                left = j+1
                right = n
                
                while left < right:
                    mid = (left + right)//2
                    if nums[mid] >= x:
                        right = mid
                    else:
                        left = mid + 1
                        
                res += left - j - 1
        return res
