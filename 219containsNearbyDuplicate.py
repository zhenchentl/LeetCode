#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-30 16:09:56
# @Author  : Damon Chen (Damon@zhenchen.me)
# @Link    : www.zhenchen.me
# @Version : $Id$
# @Description:

import os

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = dict()
        for i in range(len(nums)):
            if d.has_key(nums[i]):
                if i - d[nums[i]] <= k:
                    return True
            d[nums[i]] = i
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.containsNearbyDuplicate([1,2,3,4,1,2,3,4], 2))
