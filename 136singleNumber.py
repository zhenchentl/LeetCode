#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-14 10:48:43
# @Author  : Damon Chen (Damon@zhenchen.me)
# @Link    : www.zhenchen.me
# @Version : $Id$
# @Description:

import os

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            result = result ^ i
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([1,1,2,2,3]))
