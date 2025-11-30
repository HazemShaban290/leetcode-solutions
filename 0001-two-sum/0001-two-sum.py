class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        res=[]
        for i  in range(len(nums)):
            dic[nums[i]]=i
        for i in range(len(nums)):
            dif=target-nums[i]
            if dic.get(dif,0)!=0:
                if dic[dif]!=i:
                    return[i,dic[dif]]
                
                