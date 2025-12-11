class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        totalLen=len(nums1)+len(nums2)
        low = 0 
        high=len(nums1)
        while True:
            i= (low+high)//2 
            j =  totalLen//2 -i
            L1= nums1[i-1] if i >0 else float('-inf')
            L2=nums2[j-1] if j >0 else float('-inf')
            R1= nums1[i] if i<len(nums1) else float('inf')
            R2= nums2[j] if j<len(nums2) else float('inf')
            if L1>R2:
                high=i-1
            elif L2>R1:
                low =i+1
            else:
                break
        if totalLen%2==1:
            return min(R1,R2)
        else:
            return float((min(R1,R2)+max(L1,L2)))/2
            