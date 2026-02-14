class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #arr.sort(key=lambda y : abs(y-x))
        #return sorted(arr[:k])
        left=0
        right=len(arr)-1
        while left<=right:
            mid=(left+right)//2
            if arr[mid]==x:
                left=mid
                break
            elif arr[mid]<x:
                left=mid+1
            else:
                right=mid-1
        left=min(left,right)
        right=left+1
        print(left)
        while k>0:
            if left>=0 and right<len(arr):
                if abs(arr[left]-x) <= abs(arr[right]-x) :
                    left-=1
                else:
                    right+=1
            else:
                if left>=0:
                    left-=1
                else:
                    right+=1
            k-=1
        return arr[left+1:right]