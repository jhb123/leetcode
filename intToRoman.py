#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:13:00 2022

@author: josephbriggs
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        
        hash_table = {1:'I',
                      5:'V',
                      10:'X',
                      50:'L',
                      100:'C',
                      500:'D',
                      1000:'M',
                      900:'CM',
                      400:'CD',
                      40:'XL',
                      90:'XC',
                      4:"IV",
                      9:"IX"}
        
        
        
        num_as_str = str(num)
        roman_str = ""
        for index,l in enumerate(num_as_str):
            
            # get the leading digit and the power of ten.
            # e.g. 48 would be 4 and 1 (10^1 = 10, 4*10 = 40)
            digit = int(l)
            power = len(num_as_str)-index-1
            

            # is the digit 4,9
            if digit == 4:
                roman_str += hash_table[4*10**power]
            elif digit == 9:
                roman_str += hash_table[9*10**power]
            else:
                # is there a 5?
                is_5 = digit//5
                if is_5:
                    roman_str += hash_table[5*10**power]
                    digit= digit - 5
                # remaining digits are 1
                for d in range(digit):
                    roman_str += hash_table[1*10**power]

        
        return roman_str 
    

        
if __name__ == "__main__":
    
    sln = Solution()
    assert(sln.intToRoman(3) == "III")    
    assert(sln.intToRoman(58) == "LVIII")    
    assert(sln.intToRoman(2994) == "MCMXCIV")    
    