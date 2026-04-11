"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x.start)

        heap = [intervals[0].end]

        for i in range(1, len(intervals)):
            if intervals[i].start >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i].end)
            else:
                heapq.heappush(heap, intervals[i].end)
        
        return len(heap)