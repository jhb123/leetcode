#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 19:20:56 2022

@author: josephbriggs
"""
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        both_nums = nums1+nums2
        
        both_nums.sort()
        
        length = len(both_nums)
        
        # if odd
        if length%2:
            idx = length//2
            return both_nums[idx]
        else:
            idx_1 = length//2
            idx_2 = idx_1 - 1
            return (both_nums[idx_1]+both_nums[idx_2])/2

if __name__ == "__main__":
    
    sln = Solution()

    
    assert(sln.findMedianSortedArrays([1,3],[2])==2)