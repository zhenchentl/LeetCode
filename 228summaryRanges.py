#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-30 19:57:42
# @Author  : Damon Chen (Damon@zhenchen.me)
# @Link    : www.zhenchen.me
# @Version : $Id$
# @Description:

import os

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums == None or len(nums) == 0:
            return nums
        start, res = 0, []
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i + 1] - nums[i] > 1:
                if start == i:
                    res.append(str(nums[i]))
                else:
                   res.append(str(nums[start]) + "->" + str(nums[i]))
                start = i + 1
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.summaryRanges([0,1,2,4,5,7]))
