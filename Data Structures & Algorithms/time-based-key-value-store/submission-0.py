from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)   # key -> [(timestamp, value)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store[key]
        low, high = 0, len(pairs) - 1
        res = ""

        while low <= high:
            mid = (low + high) // 2
            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]
                low = mid + 1
            else:
                high = mid - 1

        return res