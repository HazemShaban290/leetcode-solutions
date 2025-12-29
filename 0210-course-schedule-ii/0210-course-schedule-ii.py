class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph={i:set() for i in range(numCourses)}
        for pre in prerequisites:
            graph[pre[0]].add(pre[1])
        completed=set()
        result=[]
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
            if res: 
                completed.add(course)
                result.append(course)
            return res
        for i in range(numCourses):
            if not checkCourse(i):
                return []
        return result
