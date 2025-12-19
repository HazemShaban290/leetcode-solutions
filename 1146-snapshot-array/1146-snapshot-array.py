class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.snapShotArray={}
        self.snapshot=0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index not in self.snapShotArray:
            self.snapShotArray[index]=[[self.snapshot,val]]
        else:
            if self.snapshot==self.snapShotArray[index][-1][0]:
                self.snapShotArray[index][-1][1]=val
            else:
                self.snapShotArray[index].append([self.snapshot,val])

        

    def snap(self):
        """
        :rtype: int
        """
        self.snapshot+=1
        return self.snapshot-1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        if index not in self.snapShotArray:return 0 
        start=0
        ans=-1
        end=len(self.snapShotArray[index])-1
        while start<=end:
            mid= (start+end)//2
            if self.snapShotArray[index][mid][0]<=snap_id:
                ans=self.snapShotArray[index][mid][1]
                start=mid+1
            else:
                end=mid-1
        if ans==-1:return 0
        return ans


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)