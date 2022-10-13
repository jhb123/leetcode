#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:20:45 2022

@author: josephbriggs
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortest_word = min([len(s)  for s in strs])
        number_of_words = len(strs)
        prefix = ""
        for i in range(shortest_word):
            
            compares = [s[i]  for s in strs if s[i] == strs[0][i]]
            if len(compares) < number_of_words:
                break
            else:
                prefix += strs[0][i]
        return prefix
    
        
if __name__ == "__main__":
    
    sln = Solution()
    
    assert(sln.longestCommonPrefix(["flower","flow","flight"])=="fl")
    assert(sln.longestCommonPrefix(["dog","racecar","car"])=="")
    assert(sln.longestCommonPrefix(["a"])=="a")