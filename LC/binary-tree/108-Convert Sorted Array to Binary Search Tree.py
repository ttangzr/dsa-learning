#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:19

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # method-1: inorder(将中间位置左边数字作为root)
        return self.buildTree(nums, 0, len(nums) - 1)

    def buildTree(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.buildTree(nums, left, mid - 1)
        root.right = self.buildTree(nums, mid + 1, right)
        return root