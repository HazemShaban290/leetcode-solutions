from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:set() for i in range(numCourses)}
        for pre in prerequisites:
            graph[pre[0]].add(pre[1])
        completed=set()
        visited=set()
        def checkCourse(course):
            if course in completed:
                return True
            if course in visited:
                return False
            res=True
            visited.add(course)
            for pre in graph[course]:
                res=res and checkCourse(pre)
            if res: completed.add(course)
            return res
        for i in range(numCourses):
            if not checkCourse(i):
                return False
        return True
        
        return True