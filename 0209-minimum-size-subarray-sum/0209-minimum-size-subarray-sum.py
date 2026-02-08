class Solution(object):
    def minSubArrayLen(self, target, nums):
        windSum=nums[0]
        windStar=0
        windEnd=0
        res=len(nums)+1
        flag=0
       
        while windEnd<len(nums):
            if windSum>=target:
                if windEnd-windStar+1<res:
                    flag=1
                    res=windEnd-windStar+1
                windSum-=nums[windStar]
                windStar+=1
                   
            else:
               windEnd+=1
               if windEnd>=len(nums):continue
               windSum+=nums[windEnd] 
               
             
        if flag==0:return 0
        else:return res

      