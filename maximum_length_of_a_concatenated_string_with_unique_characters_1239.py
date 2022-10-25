#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:42:16 2022

@author: josephbriggs
"""
from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        words = [""]
        maximum = 0
        for string in arr:
            for word in words:
                tentative_word = word+string
                if len(tentative_word) != len(set(tentative_word)): continue # not valid word
                words.append(tentative_word)
                maximum = max(maximum,len(tentative_word))
                
                
        return maximum
           

        

if __name__ == "__main__":
    
    sln = Solution()
    print(sln.maxLength(["un","iq","ue"]))
    print(sln.maxLength(["cha","r","act","ers"]))
    print(sln.maxLength(["abcdefghijklmnopqrstuvwxyz"]))
    print(sln.maxLength(["aa","bb"]))
    print(sln.maxLength(["ab","ba","cd","dc","ef","fe","gh","hg","ij","ji","kl","lk","mn","nm","op","po"]))
    print(sln.maxLength(["a", "abc", "d", "de", "def"]))
    