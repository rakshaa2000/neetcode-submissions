class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        inDegree = defaultdict(int)
        n = numCourses
        for pre, current in prerequisites:
            graph[pre].append(current)
            inDegree[current] += 1
        queue = deque()
        for course in range(numCourses):
            if inDegree[course] == 0:
                queue.append(course)
        while queue:
            current = queue.popleft()
            n -= 1
            for nextCourse in graph[current]:
                inDegree[nextCourse] -= 1
                if not inDegree[nextCourse]:
                    queue.append(nextCourse)
        return n == 0