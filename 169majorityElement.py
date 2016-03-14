#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-14 20:28:29
# @Author  : Damon Chen (Damon@zhenchen.me)
# @Link    : www.zhenchen.me
# @Version : $Id$
# @Description:

import os
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for x in nums:
            d[x] = d.setdefault(x, 0) + 1
            if d[x] > len(nums) / 2:
                return x

if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElement([1,2,3,3,3,3,3]))

