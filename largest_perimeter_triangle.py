#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:18:39 2022

@author: josephbriggs
"""
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # get list of unique sides and number of recurrences.

        nums.sort(reverse = True)

        # the sum of the lengths of any two sides must be greater than
        # the length of the remaining side
        for i in range(len(nums)-2):
            if (nums[i+1] + nums[i+2] > nums[i]):
                    print(sum(nums[i:i+3]))
                    return sum(nums[i:i+3])

        return 0




if __name__ == "__main__":

    sln = Solution()

    assert(sln.largestPerimeter([2, 1, 2]) == 5)
    assert(sln.largestPerimeter([1, 2, 1]) == 0)
    assert(sln.largestPerimeter([3, 2, 3, 4]) == 10)
