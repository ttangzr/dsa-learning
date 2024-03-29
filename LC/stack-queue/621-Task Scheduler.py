# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/20 09:16

from typing import List
import collections


class Solution:
    def leastInterval(self, tasks: List[str], n: int):
        freq = collections.Counter(tasks)
        # 最多执行次数(桶个数)
        maxExec = max(freq.values())
        # 具有最多执行次数的任务数量（最后一桶的任务数）
        maxCount = sum(1 for v in freq.values() if v == maxExec)
        return max((maxExec - 1) * (n + 1) + maxCount, len(tasks))


if __name__ == "__main__":
    obj = Solution()
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(obj.leastInterval(tasks, n))