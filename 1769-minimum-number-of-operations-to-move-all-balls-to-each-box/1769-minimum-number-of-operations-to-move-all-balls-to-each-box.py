class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res=[0]*len(boxes)
        count=0
        ops=0
        for i in range(len(boxes)):
            res[i]+=ops
            if boxes[i]=='1':
                count+=1
            ops+=count
        count=0
        ops=0
        for i in reversed(range(len(boxes))):
            res[i]+=ops
            if boxes[i]=='1':
                count+=1
            ops+=count
        return res
        