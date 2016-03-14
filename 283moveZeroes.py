#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-14 20:16:01
# @Author  : Damon Chen (Damon@zhenchen.me)
# @Link    : www.zhenchen.me
# @Version : $Id$
# @Description:

import os
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            j = i + 1
            if nums[i] == 0:
                while j < len(nums) and nums[j] == 0:
                    j += 1
                if j == len(nums):
                    break
                nums[i] = nums[j]
                nums[j] = 0
        return nums

if __name__ == '__main__':
    sol = Solution()
    print(sol.moveZeroes([1,2,3,0,4,5,0,0,0,7,8]))

