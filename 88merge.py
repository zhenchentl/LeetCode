#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-29 10:38:05
# @Author  : Damon Chen (Damon@zhenchen.me)
# @Link    : www.zhenchen.me
# @Version : $Id$
# @Description:

import os

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing(void)
    def merge(self, A, m, B, n):
        i = iA = iB = 0
        tmp = [0 for j in range(m + n)]
        while iA < m and iB < n:
            if A[iA] <= B[iB]:
                tmp[i] = A[iA]
                iA += 1
            else:
                tmp[i] = B[iB]
                iB += 1
            i += 1
        if iA == m:
            while i < m + n:
                tmp[i] = B[iB]
                iB += 1
                i += 1
        else:
            while i < m + n:
                tmp[i] = A[iA]
                iA += 1
                i += 1
        for i in range(m + n):
            A[i] = tmp[i]

if __name__ == '__main__':
    sol = Solution()
    print sol.merge([1,3,5],3,[2,4,6],3)
