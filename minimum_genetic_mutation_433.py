#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:37:17 2022

@author: josephbriggs
"""
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        '''
        Time complexity = O(n) where n is the length of the bank.
        Space complexity = O()

        Problem
        -------
        A gene string can be represented by an 8-character long string, with
        choices from 'A', 'C', 'G', and 'T'.

        Suppose we need to investigate a mutation from a gene string start to a
        gene string end where one mutation is defined as one single character
        changed in the gene string.

        For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
        There is also a gene bank bank that records all the valid gene
        mutations. A gene must be in bank to make it a valid gene string.

        Given the two gene strings start and end and the gene bank bank, return
        the minimum number of mutations needed to mutate from start to end.
        If there is no such a mutation, return -1.

        Note that the starting point is assumed to be valid, so it might not
        be included in the bank.

        start.length == 8
        end.length == 8
        0 <= bank.length <= 10
        bank[i].length == 8
        start, end, and bank[i] consist of only the characters
        ['A', 'C', 'G', 'T'].

        Solution
        --------
        We use a breadth first search to solve this problem. We look at the
        current layer of the 'tree' that we are on and see if the end is in
        the layer. if it is, we return the value of a counter

        We generate the next layer by iterating through the current layer and
        applying valid mutations to each element. To prevent us from revisiting
        mutations, (i.e. it would cause infinite loops), we remove mutatations
        we have already used from the bank.

        The number of mutations is equal to the depth reached by the algorithm.
        '''

        # prevents start == end bug.
        if start == end:
            return 0

        def mutate(start, bank):
            '''
            given a starting word, iterate over it and make a single letter
            replacement if it would result in a word in the bank. Return a
            dictionary of valid mutations.
            '''

            ends = {}

            for i, l1 in enumerate(start):
                for l2 in 'ACGT':
                    if l2 != l1:
                        new = start[:i] + l2 + start[i+1:]
                        if new in bank:
                            ends[new] = 0
            return ends

        # create a hash table for O(1) lookup times
        bank = {i: 0 for i in bank}
        bank[start] = 0

        # checks if the end word is even in the bank before doing much work.
        if end not in bank:
            return -1

        # initiate the first layer of the breadth first search and the counter
        ends = {start: 0}
        n = 1

        # create new layers while there are unexplored gene combinations in
        # the bank and there are possible genes to mutate from.
        while(len(bank) > 0):

            # remove the already explored genes from the bank
            for e in ends:
                bank.pop(e)

            # get the new genes by iterating through each one in the current
            # layer and add the valid unexplored mutations to it.
            new_ends = {}
            for e in ends:
                new_ends.update(mutate(e, bank))

            # if the new layer layer has nothing in it, then the end gene
            # cannot be reached from the start gene.
            if len(new_ends) == 0:
                break

            # check if the end gene is is the new layer.
            if end in new_ends:
                return n
            else:
                # set the current layer to the next layer and increment the
                # counter.
                n += 1
                ends = new_ends

        # reaches here if there are no valid mutations left to make.
        return -1


if __name__ == "__main__":
    sln = Solution()

    start = "AAAAACCC"
    end = "AACCCCCC"
    bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

    print('test case 0')
    assert sln.minMutation(start, end, bank) == 3

    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

    print('test case 1')
    assert sln.minMutation(start, end, bank) == 2

    start = "AACCTTGG"
    end = "AATTCCGG"
    bank = ["AATTCCGG", "AACCTGGG", "AACCCCGG", "AACCTACC"]

    print('test case 2')
    assert sln.minMutation(start, end, bank) == -1

    start = "AAAACCCC"
    end = "CCCCCCCC"
    bank = ["AAAACCCA", "AAACCCCA", "AACCCCCA", "AACCCCCC",
            "ACCCCCCC", "CCCCCCCC", "AAACCCCC", "AACCCCCC"]

    print('test case 3')
    assert sln.minMutation(start, end, bank) == 4

    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = []

    print('test case 4')
    assert sln.minMutation(start, end, bank) == -1
