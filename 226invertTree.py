#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-14 11:04:39
# @Author  : Damon Chen (Damon@zhenchen.me)
# @Link    : www.zhenchen.me
# @Version : $Id$
# @Description:

import os

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        tmp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = tmp
        return root
