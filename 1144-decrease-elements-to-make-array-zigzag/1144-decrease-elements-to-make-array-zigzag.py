class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1=nums[:]
        moves=0
        for i in range(len(nums1)):
            if i%2==0:
                if i<len(nums)-1  and nums1[i]<=nums1[i+1]:
                    moves+=nums1[i+1]-nums1[i]+1
                    nums1[i+1]=nums1[i]-1
            else:
                if i<len(nums)-1  and nums1[i]>=nums1[i+1]:
                    moves+=nums1[i]-nums1[i+1]+1
                    nums1[i]=nums1[i+1]-1
        nums2=nums[:]
        moves2=0
        for i in range(len(nums2)):
            if i%2==1:
                if i<len(nums2)-1  and nums2[i]<=nums2[i+1]:
                    moves2+=nums2[i+1]-nums2[i]+1
                    nums2[i+1]=nums2[i]-1
            else:
                if i<len(nums2)-1  and nums2[i]>=nums2[i+1]:
                    moves2+=nums2[i]-nums2[i+1]+1
                    nums2[i]=nums2[i+1]-1
        return min(moves,moves2)