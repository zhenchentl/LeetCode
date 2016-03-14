#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-11 19:08:16
# @Author  : Damon Chen (Damon@zhenchen.me)
# @Link    : www.zhenchen.me
# @Version : $Id$
# @Description:

import os
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = list()
        product = 1
        for x in nums:
            result.append(product)
            product *= x
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= product
            product *= nums[i]
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))

