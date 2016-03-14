#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-14 13:32:18
# @Author  : Damon Chen (Damon@zhenchen.me)
# @Link    : www.zhenchen.me
# @Version : $Id$
# @Description:

import os

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # while num > 9:
        #     s = num
        #     num = 0
        #     while s:
        #         num += s % 10
        #         s /= 10
        # return num
        # *****************************
        # while num > 9:
        #     num = sum([int(x) for x in str(num)])
        # return num
        # *****************************
        return 0 if num == 0 else (num - 1) % 9 + 1

if __name__ == '__main__':
    sol = Solution()
    print(sol.addDigits(123456))
