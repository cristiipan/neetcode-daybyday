class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # we sort the list to remove duplicates
        if nums[0] > 0 or nums[-1] < 0:
            return []

        result = []
        for i in range(len(nums) - 2):  # i->p->q,给p q各留一个位置
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # if nums[i] == nums[i + 1]:  # 记住这个错误写法！在for循环里手动改i没有效果，for循环下一轮还是会按自己的逻辑递增i
            #     i += 1

            p = i + 1
            q = len(nums) - 1

            while p < q:
                total = nums[i] + nums[p] + nums[q]
                if total < 0:
                    p += 1
                elif total > 0:
                    q -= 1
                else:
                    result.append([nums[i], nums[p], nums[q]])
                    p += 1
                    q -= 1
                    while p < q and nums[p] == nums[p - 1]:  # 前面要跳过重复的i，这里也要跳过重复的qp
                        p += 1
                    while p < q and nums[q] == nums[q + 1]:
                        q -= 1
        
        return result