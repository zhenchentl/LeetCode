#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-14 20:12:19
# @Author  : Damon Chen (Damon@zhenchen.me)
# @Link    : www.zhenchen.me
# @Version : $Id$
# @Description:

import os

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = dict()
        for x in nums:
            if d.has_key(x):
                d[x] += 1
            else:
                d[x] = 1
        for k, v in d.items():
            if v > 1:
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.containsDuplicate([1,1,2,3,4]))
