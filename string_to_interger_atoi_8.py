#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:57:15 2022

@author: josephbriggs
"""
import re

class Solution:
    def myAtoi(self, s: str) -> int:
        # Python supports ints greater than 31 bits. This problem can be 
        # 'solved' by checking if x > 2147483648 or whatever, but this wouldn't
        # work in the scenario that is described in 8. String to Integer (atoi)
        # as it would cause an overflow.
        
        # find the substring which starts with white space, - or and nothing 
        # followed by any number of numerals.
        num_str = re.findall("^(\s*-\s*\d+|\s*\+\d+|\s*\d+)",s)
        
        # this is the string which represents the largest 31 bit number
        max_int_str = "2147483648"
        if num_str:

            # format the string by removing white spaces and leading zeros. 
            num_str = num_str[0]
            num_str = num_str.replace(" ","")
            numbers_only = re.findall("\d+", num_str)[0]
            numbers_only = numbers_only.lstrip("0")
            
            # check if the number is positive or negative. This needs to be 
            # done since the limits are -2**31 to 2**31 - 1 
            is_pos = num_str[0] != '-'
            
            # if the length of the numbers string is bigger than the max length,
            # return the maximum numbers depending on the sign.
            if len(numbers_only) > len(max_int_str):
                return -2147483648 if not is_pos else 2147483647
            
            # if the length of the numbers string is equal to the max length...
            elif len(numbers_only) == len(max_int_str):
                # return the max numbers if the the all but right most digit
                # correspond to a bigger integer
                cond = int(numbers_only[0:-1]) > int(max_int_str[0:-1])
                if cond: return -2147483648 if not is_pos else 2147483647
                # If all the left but one digit are the the maximum valid digit
                # check if the right most digit exceeds the largest permissable
                # number and check its sign. Return the clamp value if this is
                # true
                cond = int(numbers_only[0:-1]) == int(max_int_str[0:-1])
                
                if int(numbers_only[-1]) >= 7 and is_pos and cond: return 2147483647
                if int(numbers_only[-1]) >= 8 and not is_pos and cond: return -2147483648
                
            # if the value is not exceeding the clamp value, just return it.
            return(int(num_str))
        else:
            # invalid strings return 0.
            return 0
        
        # num = 0
        
        # for letter in s:
            
        #     num += 
        
        # return s

if __name__ == "__main__":
    sln = Solution()
    assert(sln.myAtoi("42") == 42)
    assert(sln.myAtoi("-42") == -42)
    # assert(sln.myAtoi("+2147483648") == 2147483648)
    assert(sln.myAtoi("-2147483648") == -2147483648)

    
    assert(sln.myAtoi("-  0000000000012345678") == -12345678)
    assert(sln.myAtoi("    +42 with words") == 42)
    assert(sln.myAtoi("words and 987") == 0)
    assert(sln.myAtoi("   +0 123") == 0)
    assert(sln.myAtoi("  +  413") == 0)
    assert(sln.myAtoi("1095502006p8") == 1095502006)
    assert(sln.myAtoi("2147483800") == 2147483647)
    
    assert(sln.myAtoi("-91283472332")== -2147483648)
    assert(sln.myAtoi(" 1192820738r2") == 1192820738)
    assert(sln.myAtoi("2147483648") == 2147483647)
    assert(sln.myAtoi("2147483646") == 2147483646)