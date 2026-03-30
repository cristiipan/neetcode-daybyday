"""
the strategy we want to use here:
the entire cycles sequence can be devided into multiple slots, each slot has (n+1) cycles
because everytime we finish a task, we need to wait at least n cycles to do a identical task
we first maintain a heap that automatically regulars all the tasks' frequency
because at the beginning of each task, we should always pick the most frequent task
as long as there's still task that need to re-enter the heap after the current slot
we add (n+1) cycles to the final result
if there's no tasks to re-enter after this slot
we add the current acumulated cycles to the final result
"""
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic_tasks = {}  # design a dictionary to journal down the tasks' frequencies
        for task in tasks:
            dic_tasks[task] = dic_tasks.get(task, 0) + 1  # task is key, freqs is value, default set to 0
        
        freqs = []  # a heap of freqs, freqs[0] is the least frequent
        for freq in dic_tasks.values():
            heapq.heappush(freqs, -freq)  # -freqs[0] would be the most frequent task

        result = 0     # all the cycles we need in the end

        while freqs:   # meaning there's still unfinished task
                       # 每次循环必须走到底完成整个窗口，更新完result之后才回到while入口判断freqs是否为空，决定要不要再走一轮
            cycle = 0  # cycle we finished in this slot (each slot contains [n + 1] cycles)
            temp = []  # all the tasks remained after this slot

            for i in range(n + 1):  # iterate through the current slot and assign task to each spot
                                    # even if there's an idle, it will be counted
                if freqs:           # as long as there's a task remaining
                    freq = heapq.heappop(freqs)     # pop it out and read its frequency
                    if freq + 1 < 0:                # remember the frequency we pushed in is negative
                        temp.append(freq + 1)       # remaining tasks get pushed into temp[]
                    cycle += 1      # 1 task gets finished, cycle + 1
            
            for f in temp:
                heapq.heappush(freqs, f)

            if freqs:
                result += n + 1
            else:
                result += cycle
        
        return result
