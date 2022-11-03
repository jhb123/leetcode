#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:19:04 2022

@author: josephbriggs
"""
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        '''
        2131. Longest Palindrome by Concatenating Two Letter Words

        Problem
        -------
        You are given an array of strings words. Each element of words 
        consists of two lowercase English letters.

        Create the longest possible palindrome by selecting some elements from
        words and concatenating them in any order. Each element can be 
        selected at most once.

        Return the length of the longest palindrome that you can create. 
        If it is impossible to create any palindrome, return 0.

        A palindrome is a string that reads the same forward and backward.
        

        Solution
        --------
        Creating a hashmap gives is O(1) look up times. Iterate through the
        word list and count the number of times a word is in it.
        
        Next, go through the hash map and see if for each word, there is the 
        corresponding reversed word. If there is, then these letters can be 
        added to the palidrome string's lenght. Finally, there needs to be 
        a check that a double letter e.g. "aa" is in the word's centre.

        Solution Complexity
        -------------------
        Time complexity: O(n) where n is the length of the words list.
        Space complexity: O(26^2).
        
        Reasoning
        there are only 26 letters in the alphabet, and so there are 26^2 
        combinations of letters. Iterating over words takes n time, and storing
        this many words takes O(26^2) space in a hash map.
        '''
        word_hash_table = {}
        centre_hash_table = {}
        
        
        for word in words:
            if word not in word_hash_table:
                word_hash_table[word] = 1
            else:
                word_hash_table[word] +=1
        
        length = 0
        left_over = 0
        for word in word_hash_table:
            word_rev = word[::-1]
            if word == word_rev:
                # get number of pairs, this represents 4 letters
                num_recs = word_hash_table[word]
                length += 4*(num_recs//2)
                # if there are an odd number of "aa" type words, then one can
                # be inserted into the middle of the palidrome.
                if num_recs%2:
                    # 2 letters
                    left_over = 2
            else:
                forward_recs = word_hash_table[word]
                # check if the backwards version is in the hashtable. If it is
                # use the smaller number of recurrences as the number in the 
                # final word and set the values in the hash table to show that
                # the letters have been used.
                if word_rev in word_hash_table:
                    backward_recs = word_hash_table[word_rev]
                    # each match represents 2 letters and 2 words
                    length += 4*min(forward_recs,backward_recs)
                    word_hash_table[word] = 0
                    word_hash_table[word_rev] = 0
        
        return length+left_over

    
words = ["lc","cl","gg","lc"]
sln = Solution()
assert sln.longestPalindrome(words) == 6
words = ["ab","ty","yt","lc","cl","ab"]
assert sln.longestPalindrome(words) == 8
words = ["cc","ll","xx"]
assert sln.longestPalindrome(words) == 2
