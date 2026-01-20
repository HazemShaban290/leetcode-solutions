class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ballBoxes=set()

        res=[]
        for i in range(len(boxes)):
            if boxes[i]=='1':
                ballBoxes.add(i)
        for i in range(len(boxes)):
            operations=0
            for ballIdx in ballBoxes:
                operations+=abs(i-ballIdx)
            res.append(operations)
        return res