#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:50:18 2022

@author: josephbriggs
"""

from typing import List



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        hash_table = {n:[] for n in nums}
        
        for n in nums:
            hash_table[n].append(n)
        
        target = 0
        triplets = set()
        keys = set(nums)

        for n1 in keys:
            num_repeats = len(hash_table[n1])

            if num_repeats >= 3 and sum(hash_table[n1][0:3]) == target:
                ls = [n1,n1,n1]
                tp = tuple(ls)
                triplets.add(tp)

            if  num_repeats >= 2:
                n2 = -n1 -n1 + target
                if n2 in hash_table and n2 != n1:
                    ls = [n1,n1,n2]
                    ls.sort()
                    tp = tuple(ls)
                    triplets.add(tp)
            
            if num_repeats >= 1:
                for n2 in keys:           
                    n3 = - n1 - n2 + target
                    if n1 != n2 and n2 != n3 and n3 != n1 and n3 in hash_table:
                        ls = [n1,n2,n3]
                        ls.sort()
                        tp = tuple(ls)
                        triplets.add(tp)
                        
        return triplets
                    

if __name__ == "__main__":
    
    sln = Solution()

    # print(sln.threeSum([-1,0,1,2,-1,-4]))
    # print(sln.threeSum([0,1,1]))
    # print(sln.threeSum([0,0,0]))
    # print(sln.threeSum([0,0,0,0]))
    # print(sln.threeSum([1,2,-2,-1]))
    # print(sln.threeSum([-1,0,1]))
    # print(sln.threeSum([-1,0,1,0]))
    # print(sln.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
    # [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
    print(sln.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))

    # [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]