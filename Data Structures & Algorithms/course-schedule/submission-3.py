class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we initialize a map to represent all courses and their prerequisites
        # i [0, 1, 2,...numCourses-1] is the courses
        # we initialize all courses' prerequisites to be an empty list, and map the course to them
        preMap = { i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:      # 解包
            preMap[crs].append(pre)
        
        # a visitSet to store all visited courses along the current DFS path
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False        # if we are visiting a course twice, meaning there's a loop and this course cannot be completed
            if preMap[crs] == []:
                return True         # if a course has not prerequisites, it can definitely be completed
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):        # if its prerequisite itself returns False then we can retun False immediately
                    return False
            # before return True we need to remove current course from visitSet cause the current DFS path ended and we are no longer visiting this course
            visitSet.remove(crs)
            # also we set the prerequisites list of the course that can be finished to empty, marking that it can be finished
            # 有了这一步 即使有共享依赖的course 同一个node也不会被revisit 因为在上面的判断里就会提前结束
            # 这步剪枝保证已检查过的节点不会被重复遍历
            preMap[crs] = []
            return True

        # 必须用for loop 避免有互相不衔接的课 / 整个图未必全部连通
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True