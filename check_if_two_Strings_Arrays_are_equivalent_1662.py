#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:50:51 2022

@author: josephbriggs
"""
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        word1 = ''.join(word1)
        word2 = ''.join(word2)
        
        return word1 == word2
        
        
        
if __name__ == "__main__":
    sln = Solution()
    assert(sln.arrayStringsAreEqual(["ab", "c"],["a", "bc"])==True)