#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 00:10:32 2022

@author: josephbriggs
"""

import seaborn as sns
import random

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i = 0
        j = len(height)-1
        max_area = min(height[i],height[j])*(j - i)
        while i < j:
            # print(i,j)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
            
            area = min(height[i],height[j])*(j - i)
            
            if area > max_area:
                max_area = area
        
        return max_area
            
        

    
    

    
        
if __name__ == "__main__":
    
    sln = Solution()
    assert(sln.maxArea([1,8,6,2,5,4,8,3,7]) == 49)
    
    