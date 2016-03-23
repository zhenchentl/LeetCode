#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-23 19:55:45
# @Author  : Damon Chen (Damon@zhenchen.me)
# @Link    : www.zhenchen.me
# @Version : $Id$
# @Description:

import os
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits.insert(0,1)
        return digits

if __name__ == '__main__':
    sol = Solution()
    print sol.plusOne([])
