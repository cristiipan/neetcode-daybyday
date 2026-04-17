class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)     # all the edges, course - prerequisite relation

        res = []                        # final result to return
        visitSet = set()                # a set to store all visited courses / nodes on current dfs path

        def dfs(crs):
            if crs in visitSet:         # if we are revisiting same node, then there's a loop and this course cannot be finished, return False immediately
                return False
            if preMap[crs] == []:       # if there's no prerequisite / this course has been proved to be able to be finished, return True immediately
                if crs not in res:
                    res.append(crs)
                return True
            
            visitSet.add(crs)           # if it doesn't fall into those 2 situations, then we begin a dfs path from this node, we add it to our current path
            for pre in preMap[crs]:     # we run dfs on all of its prerequisites / neighbors
                if not dfs(pre):
                    return False        # if any of them cannot be finished, we return False immeditely
            visitSet.remove(crs)        # after running dfs on all neighbors and they all return True, before we return True we remove this node from current path
            
            res.append(crs)
            
            preMap[crs] = []            # we set its prerequisites to empty list meaning this course can be finished (这种做法隐式地代表了第三种状态)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res