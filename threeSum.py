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
        
        target = 255
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
    # print(sln.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))
    print(sln.threeSum([-43,57,-71,47,3,30,-85,6,60,-59,0,-46,-40,-73,53,68,-82,-54,88,73,20,-89,-22,39,55,-26,95,-87,-57,-86,28,-37,43,-27,-24,-88,-35,82,-3,39,-85,-46,37,45,-24,35,-49,-27,-96,89,87,-62,85,-44,64,78,14,59,-55,-10,0,98,50,-75,11,97,-72,85,-68,-76,44,-12,76,76,8,-75,-64,-57,29,-24,27,-3,-45,-87,48,10,-13,17,94,-85,11,-42,-98,89,97,-66,66,88,-89,90,-68,-62,-21,2,37,-15,-13,-24,-23,3,-58,-9,-71,0,37,-28,22,52,-34,24,-8,-20,29,-98,55,4,36,-3,-9,98,-26,17,82,23,56,54,53,51,-50,0,-15,-50,84,-90,90,72,-46,-96,-56,-76,-32,-8,-69,-32,-41,-56,69,-40,-25,-44,49,-62,36,-55,41,36,-60,90,37,13,87,66,-40,40,-35,-11,31,-45,-62,92,96,8,-4,-50,87,-17,-64,95,-89,68,-51,-40,-85,15,50,-15,0,-67,-55,45,11,-80,-45,-10,-8,90,-23,-41,80,19,29,7]))

    # [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]