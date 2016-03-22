#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-22 14:59:04
# @Author  : Damon Chen (Damon@zhenchen.me)
# @Link    : www.zhenchen.me
# @Version : $Id$
# @Description:

import os

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None:
            return 0
        if len(nums) <= 1:
            return len(nums)
        index = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[index] = nums[i + 1]
                index += 1
        return index

if __name__ == '__main__':
    sol = Solution()
    print sol.removeDuplicates([1,1,2])
