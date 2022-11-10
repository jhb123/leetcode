#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:41:50 2022

@author: josephbriggs
"""
from collections import deque
from random import randint
import string
import time

class Solution:
    def removeDuplicates_deque(self, s: str) -> str:
        # linear in time
        new_s = deque()
        for l in s:
            if len(new_s) == 0:
                new_s.append(l)
            elif new_s[-1] == l:
                new_s.pop()
            else:
                new_s.append(l)
        return ''.join(new_s)

    def removeDuplicates_string(self, s : str) -> str:
        # linear in time
        new_str = ""
        for l in s:
            if new_str == "":
                new_str += l
            elif new_str[-1] == l:
                new_str= new_str[:-1]
            else:
                new_str += l
        return new_str


    def removeDuplicates_rec(self, s : str) -> str:
        # quadratic in time
        for i in range(len(s)-1):
            letter_1 = s[i]
            letter_2 = s[i+1]
            if letter_1 == letter_2:
                new_s = s[:i] + s[i+2:]
                return self.removeDuplicates_rec(new_s)
        return s


if __name__ == "__main__":

    sln = Solution()
    test_case = ''.join([ string.ascii_lowercase[randint(0, 25)] for i in range(10000)])

    tic = time.perf_counter()
    total_time = 0
    reps = 100
    for i in range(reps):
        tic = time.perf_counter()
        tutorial = sln.removeDuplicates_string(test_case)
        toc = time.perf_counter()
        total_time  += toc-tic
    print(f'string method: {total_time/reps:.5e}s')
    for i in range(reps):
        tic = time.perf_counter()
        tutorial = sln.removeDuplicates_deque(test_case)
        toc = time.perf_counter()
        total_time  += toc-tic
    print(f'deque method: {total_time/reps:.5e}s')
    for i in range(reps):
        tic = time.perf_counter()
        tutorial = sln.removeDuplicates_rec(test_case)
        toc = time.perf_counter()
        total_time  += toc-tic
    print(f'recursive method: {total_time/reps:.5e}s')