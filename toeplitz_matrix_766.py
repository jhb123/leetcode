#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 10:42:29 2022

@author: josephbriggs
"""
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        '''
        Consider the following Toeplitz matrix
        (https://en.wikipedia.org/wiki/Toeplitz_matrix)
        a b c d
        e a b c
        f e a b
        g f e a
        h g f e

        This function splits the matrix into 2 parts. The first part looks like
        this:
            a b c d
              a b c
                a b
                  a

        and the second part looks like this:
            e
            f e
            g f e
            h g f e

        This function interates in a diagonal manner over the elements in the
        above triangles and checks if the diagonal elements are equal.

        Time complexity = O(n*m) where n and m are the number of rows and
        columns respectively of the matrix since each element of the matrix
        is at most looked at once. Beats 95% of leetcode submissions.

        Space complexity = O(1). A recursive version of this would take O(k)
        '''

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # pass over columns
        for i in range(num_cols):
            diagonal_value = matrix[0][i]
            for j in range(num_rows):
                if i + j > num_cols-1:
                    break  # indexing ends at the size - 1
                if matrix[j][i+j] != diagonal_value:
                    return False

        # pass over rows:
        for i in range(1, num_rows):  # skip the first row to avoid duplicate work
            diagonal_value = matrix[i][0]
            for j in range(num_cols):
                if i + j > num_rows-1:
                    break
                if matrix[i+j][j] != diagonal_value:
                    return False

        return True


if __name__ == "__main__":
    sln = Solution()

    matrix = [[1, 2, 3, 4],
              [5, 1, 2, 3],
              [9, 5, 1, 2]]

    assert sln.isToeplitzMatrix(matrix)
