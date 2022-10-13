#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:09:30 2022

@author: josephbriggs
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # slow way
        # for i,x in enumerate(nums):
        #     for j,y in enumerate(nums[i+1:]):
        #         if x+y == target:
        #             return [i,i+j+1]
        
        # fast way: hash table
        hashtable = {}
        for i,num in enumerate(nums):
            delta = target - num
            if num in hashtable:
                return [hashtable[num],i]
            else:
                hashtable[delta] = i
                
if __name__ == "__main__":

    sln = Solution()

    assert(sln.twoSum([2,7,11,15], target = 9) == [0,1])
    assert(sln.twoSum([3,2,4], target = 6) == [1,2])
    assert(sln.twoSum([3,3], target = 6) == [0,1])

                