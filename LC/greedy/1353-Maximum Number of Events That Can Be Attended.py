# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/31 19:32


from typing import List
import heapq


class Solution:
    def maxEvents(self, events: List[List[int]]):
        # method-1: greedy + 优先队列
        # 第i天，end小的优先开会为最优
        # 按开始时间降序
        events.sort(key=lambda x: x[0], reverse=True)
        n = max(j for i in events for j in i)   # 最晚end时间
        heap = []
        res = 0
        for i in range(1, n + 1):
            # 按start, 将能开的会议都pop出来，给heap
            while events and events[-1][0] <= i:
                heapq.heappush(heap, events.pop()[1])
            # end小的优先pop（小根堆）
            while heap:
                earliest = heapq.heappop(heap)
                if earliest >= i:   # 结束前
                    res += 1
                    break
        return res


if __name__ == '__main__':
    obj = Solution()
    # events = [[1, 2], [2, 3], [3, 4], [1, 2]]
    # events = [[1,2],[1,2],[3,3],[1,5],[1,5]]
    events = [[1,5],[1,5],[1,5],[2,3],[2,3]]
    print(obj.maxEvents(events))