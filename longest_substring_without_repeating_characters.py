#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:38:10 2022

@author: josephbriggs
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        max_length = 0
        used_letter_hashtable = {}
        
        for i,letter in enumerate(s):
            
            # has the letter been used before the start of the window
            if letter in used_letter_hashtable and used_letter_hashtable[letter]>=start:
                start = used_letter_hashtable[letter]+1
            else:
                max_length = max(max_length,i-start+1)
            
            used_letter_hashtable[letter] = i
        print(max_length)
        return max_length
             
    
if __name__ == "__main__":

    sln = Solution()

    assert(sln.lengthOfLongestSubstring("abcabcbb") == 3)
    assert(sln.lengthOfLongestSubstring("bbbbb") == 1)
    assert(sln.lengthOfLongestSubstring("pwwkew") == 3)
    assert(sln.lengthOfLongestSubstring(" ") == 1)
    assert(sln.lengthOfLongestSubstring("") == 0)
    assert(sln.lengthOfLongestSubstring("au") == 2)
    assert(sln.lengthOfLongestSubstring("tmmzuxt") == 5)
