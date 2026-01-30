"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employeesTree={}
        for emp in employees:
            employeesTree[emp.id]=emp
        queue=deque([id])
        totalImportance=0
        while queue:
            nextEmp=queue.popleft()
            totalImportance+=employeesTree[nextEmp].importance
            for sub in employeesTree[nextEmp].subordinates:
                queue.append(sub)
        return totalImportance