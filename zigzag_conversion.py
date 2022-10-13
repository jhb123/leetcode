#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:34:08 2022

@author: josephbriggs
"""
from itertools import cycle,chain

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        strings = ["" for i in range(numRows)]
        
        zig_zag_iter = cycle(chain(range(numRows-1),range(numRows-1,0,-1)))
        for letter,row in zip(s,zig_zag_iter):
            for r in range(numRows):
                if r ==row:        
                    strings[r] = strings[r] +  letter
        
        output = ""
        for string in strings:
            output += string
        return output
            
            

if __name__ == "__main__":
    
    sln = Solution()
    assert(sln.convert("PAYPALISHIRING",numRows = 3) == "PAHNAPLSIIGYIR")
    assert(sln.convert("PAYPALISHIRING",numRows = 4) == "PINALSIGYAHRPI")
    assert(sln.convert("A",numRows = 1) == "A")