class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 按 position 从大到小配对排序
        pairs = sorted(zip(position, speed), reverse = True)
        stack = []

        for pos, speed in pairs:
            time = (target - pos) / speed
            if not stack or time > stack[-1]:
                stack.append(time)
                # 否则 time <= stack[-1]，追上了，不入栈

        return len(stack)