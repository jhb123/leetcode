#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 11:20:26 2022

@author: josephbriggs
"""
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        
        val = nums[0]+nums[1]+nums[2]
        for i,n1 in enumerate(nums[:-2]):
            j , k = i+1,len(nums) - 1 # set the numbers to the adjacent and end number
            
            while j < k:
            
                
                val_tentative = nums[i]+nums[j]+nums[k]
                if abs(val_tentative-target) < abs(val - target):
                    val = val_tentative
                if val_tentative < target:
                    j += 1
                elif val_tentative > target:
                    k -= 1
                else:
                    return val
        return val
            
            
if __name__ == "__main__":
    
    sln = Solution()
    # print(sln.twoSumClosest([97,102,200], 297))
    # print(sln.twoSumClosest([-1,2,1,-4], 100))
    assert(sln.threeSumClosest([-1,2,1,-4], 1) == 2)
    # # print(sln.threeSumClosest([0,0,0], 0))
    assert(sln.threeSumClosest([1,1,1,0], 100) == 3)
    # print("______________")
    assert(sln.threeSumClosest([1,1,1,0], -100) == 2)
    # print("______________")
    assert(sln.threeSumClosest([0,3,97,102,200], 300) == 300)
    # print("______________")
    assert(sln.threeSumClosest([-43,57,-71,47,3,30,-85,6,60,-59,0,-46,-40,-73,53,68,-82,-54,88,73,20,-89,-22,39,55,-26,95,-87,-57,-86,28,-37,43,-27,-24,-88,-35,82,-3,39,-85,-46,37,45,-24,35,-49,-27,-96,89,87,-62,85,-44,64,78,14,59,-55,-10,0,98,50,-75,11,97,-72,85,-68,-76,44,-12,76,76,8,-75,-64,-57,29,-24,27,-3,-45,-87,48,10,-13,17,94,-85,11,-42,-98,89,97,-66,66,88,-89,90,-68,-62,-21,2,37,-15,-13,-24,-23,3,-58,-9,-71,0,37,-28,22,52,-34,24,-8,-20,29,-98,55,4,36,-3,-9,98,-26,17,82,23,56,54,53,51,-50,0,-15,-50,84,-90,90,72,-46,-96,-56,-76,-32,-8,-69,-32,-41,-56,69,-40,-25,-44,49,-62,36,-55,41,36,-60,90,37,13,87,66,-40,40,-35,-11,31,-45,-62,92,96,8,-4,-50,87,-17,-64,95,-89,68,-51,-40,-85,15,50,-15,0,-67,-55,45,11,-80,-45,-10,-8,90,-23,-41,80,19,29,7], 255) == 255)
    # # print("______________")
    assert(sln.threeSumClosest([-23,-67,32,21,-65,46,73,42,93,9,-61,-79,-51,61,-15,49,92,-34,50,1,26,-12,68,-97,-17,51,-55,75,-56,-95,-70,-42,91,-18,-64,20,33,-20,19,61,-89,81,-73,82,-23,-65,51,-88,15,-48,24,34,0,-24,37,22,28,-67,-25,-61,-57,-74,65,50,-66,24,99,80,44,85,20,-4,-9,-81,87,-82,-100,51,-83,9,-31,37,23,-61,53,-14,-51,88,56,27,42,-52,-97,37,36,-59,-45,95,46,-1,-100,-38,66,44,27,-97,12,-43,84,-53,93,18,-40,-38,34,85,53,-50,-14,-6,98,-77,-17,50,-65,52,-46,-94,49,72,-2,-82,45,-39,-58,67,82,63,95,-32,47,15,-20,46,5,17,-40,-95,97,-9,11,8,-51,-24,-50,-37,-72,-57,26,26,19,71,-42],-87) == - 87)

    assert(sln.threeSumClosest([147,465,-917,-321,551,982,-967,-672,670,-859,-776,290,-406,223,123,-266,730,339,792,588,138,822,474,-615,386,-392,559,364,124,829,-505,553,-284,-458,-826,-791,-67,-798,932,-828,-739,65,-782,-159,363,-123,893,-992,-662,-65,-352,-649,-357,780,-690,-584,-660,-427,802,113,856,34,-145,-97,-8,488,467,-24,967,96,-915,309,-931,989,-789,886,-568,451,965,-344,917,-994,865,-537,241,-761,812,768,648,594,-702,-640,845,350,-408,984,870,246,-107,508,-860,-298,514,349,960,-663,-616,-87,566,-449,161,522,293,270,-276,928,-612,117,-263,721,-692,-712,995,729,115,463,328,397,-781,-253,782,-542,71,919,286,-732,-271,401,-820,51,-232,-170,-189,154,-487,-221,632,860,38,-224,839,-227,656,194,-331,-422,-997,784,640,-367,385,202,520,-553,-44,208],1826) == 1826)
#####
# really slow method
#####

# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:


        # nums.sort()
        # output_set = set()
        
        # for i,n in enumerate(nums):
        #     for j,m in enumerate(nums):
        #         for k,o in enumerate(nums):
        #             if i == j or i == k or j == k:
        #                 pass
        #             else:
        #                 output_set.add(n+m+o)
        
        # # print(output_set)
        # diff_list = [(i,abs(i-target)) for i in output_set]
        # # print(diff_list)

        # num_min,err_min = diff_list[0]
        
        # for num,err in diff_list:
        #     if err < err_min:
        #         num_min = num
        #         err_min = err
        #     if err_min == 0:
        #         break 
            
        # return num_min
    
    
#####
# 2d tests
#####
# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:

        # nums.sort()
        
        # num_matrix = [ [] for i in nums]
        
        # 2-d version
        
        # for i,n0 in enumerate(nums):
        #     for j,n1 in enumerate(nums):
        #         if i == j:
        #             num_matrix[i].append(None)
        #         else:
                    
        #             num_matrix[i].append(n0+n1-target)
        
        # for row,_ in enumerate(num_matrix):
        #     row_str = [f"{str(a):>3}"  if a is not None else "   " for a in num_matrix[row]]
        #     print(row_str)
            
            
        # i = 0
        # j = 1
        # k = 0
        # while True:
        #     print(f"step {k}")
        #     if i == len(nums)-1 and j == len(nums)-1:
        #         val = nums[i]+nums[j]-target
        #         break
            
        #     val = nums[i]+nums[j]-target
        #     print(i,j,val)
        #     if val == 0:
        #         break
        #     else:
        #         i_tentative = min(i + 1,len(nums)-1)
        #         if i_tentative < j:
        #             j_tentative = min(j + 1,len(nums)-1)
                
        #             val_1 = abs(nums[i_tentative]+nums[j]-target)
        #             val_2 = abs(nums[i]+nums[j_tentative]-target)
        #             if abs(val) < val_1 and abs(val) < val_2:
        #                 break
        #             if val_1 <= val_2:
        #                 i = i_tentative
        #             if val_2 < val_1:
        #                 j = j_tentative
        #         else:
        #             if j+1 < len(nums):
        #                 j += 1
        #             else:
        #                 break
                
        #     k += 1 
        