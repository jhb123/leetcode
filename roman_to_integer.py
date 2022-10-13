#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 13:00:33 2022

@author: josephbriggs
"""

class Solution:
    def romanToInt(self, s: str) -> str:
            
        hash_table = {'I':1,
                      'V':5,
                      'X':10,
                      'L':50,
                      'C':100,
                      'D':500,
                      'M':1000,
                      'CM':900,
                      'CD':400,
                      'XL':40,
                      'XC':90,
                      "IV":4,
                      "IX":9}
        
        s2 = s +' ' #add a dummy character
        num = 0
        skip = False
        for letter_1,letter_2 in zip(s,s2[1:]):
            if skip:
                skip = False
            else:
                two_letter_str = letter_1+letter_2
                if two_letter_str in hash_table:
                    num +=hash_table[two_letter_str]
                    skip = True
                else:
                    num +=hash_table[letter_1]
        return num
            
    

        
if __name__ == "__main__":
    
    sln = Solution()
    assert(sln.romanToInt("III") == 3)
    assert(sln.romanToInt("LVIII") == 58)
    assert(sln.romanToInt("MCMXCIV") == 1994)

    