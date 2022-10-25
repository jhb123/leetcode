#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:17:56 2022

@author: josephbriggs
"""

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        
        x = abs(x)
        
        num = 0
        
        max_num = 2**31
        
        while(x):
            if num > max_num/10:
                return 0
            elif num == max_num/10 and x % 10 == 7:
                return 0
            else:
                num *= 10
                num += (x % 10)
                x = x//10
            
            
        return sign*num #if num<2**31 else 0
    
if __name__ == "__main__":
    sln = Solution()
    # print(sln.reverse(10211))
    print(sln.reverse(-123))
    print(sln.reverse(120))
    print(sln.reverse(1534236469))