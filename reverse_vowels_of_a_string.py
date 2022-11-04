#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:07:18 2022

@author: josephbriggs
"""
from collections import deque


class Solution:
    def reverseVowels(self, s: str) -> str:
        '''
        Problem
        --------
        Given a string s, reverse only all the vowels in the string and return
        it.

        The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in
        both lower and upper cases, more than once.

        Solution
        --------
        create a set of the ascii characters which we want to reverse. The set
        gives O(1) time look up times

        Create a stack to give O(1) time look up for the next letter to
        add to the final string. Iterate through the string adding the vowels
        to the stack. This is an order O(n) in time.

        Iterate through the list again to create a new string. Every time a
        vowel is encountered, pop the vowel on the stack.

        Thus, this is an O(n) solution.

        The stack and new word requires O(n) space.
        '''
        vowels = set("aeiouAEIOU")

        vowel_stack = deque()

        for letter in s:
            if letter in vowels:
                vowel_stack.append(letter)

        new_s = []

        for letter in s:
            if letter in vowels:
                new_s.append(vowel_stack.pop())
            else:
                new_s.append(letter)

        new_s = ''.join(new_s)

        return new_s


if __name__ == "__main__":

    sln = Solution()

    assert sln.reverseVowels("hello") == "holle"
    assert sln.reverseVowels("leetcode") == "leotcede"
    assert sln.reverseVowels("") == ""
