#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 09:50:47 2022

@author: josephbriggs
"""
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        '''
        Problem:
            You have a 2-D grid of size m x n representing a box, and you have
            n balls. The box is open on the top and bottom sides.

            Each cell in the box has a diagonal board spanning two corners of
            the cell that can redirect a ball to the right or to the left.

            A board that redirects the ball to the right spans the top-left
            corner to the bottom-right corner and is represented in the grid
            as 1.

            A board that redirects the ball to the left spans the top-right
            corner to the bottom-left corner and is represented in the grid as
            -1.

            We drop one ball at the top of each column of the box. Each ball
            can get stuck in the box or fall out of the bottom.
            A ball gets stuck if it hits a "V" shaped pattern between two
            boards or if a board redirects the ball into either wall of the box.

            Return an array answer of size n where answer[i] is the column
            that the ball falls out of at the bottom after dropping the ball
            from the ith column at the top, or -1 if the ball gets stuck in the
            box.

        Solution:
            This problem can be solved by simulating the ball's position. You
            need to check if the element of the grid that the ball is currently
            on would cause it to become blocked. A left-moving cell is
            represented by -1 and a right-moving cell is represented by 1. This
            means that the next position is its current position + the value in
            the cell. You need to check that this stays within the grid as the
            sides are blocked, and you need to check if the ball is in a V
            groove. To check if its in a groove, check the adjacent square
            in the direction the ball would move is not of the opposite
            direction e.g. a left-moving square needs to be next to a
            right-moving square.
            
            This is implemented using an iterative depth-first search.


        Complexity:
            time complexity = O(n*m) where n = number of rows and m = the 
            number of columns
            Space complexity = O(1)

            Each starting position has to be checked, this gives you the m
            in the time complexity.
            on a row by row basis, you check if the ball can move forward.
            This requires you to check one element of the the grid, so this
            gives you the n in the time complexity.
            No additional storage is needed for this function, so it has a
            space complexity of O(1)
        '''
        
        width = len(grid[0])

        output_columns = []

        for ball_pos in range(width):

            is_valid = True
            for row in grid:
                direction = row[ball_pos]
                next_idx = ball_pos+direction

                if next_idx >= width:
                    is_valid = False
                    break
                elif next_idx < 0:
                    is_valid = False
                    break
                elif row[ball_pos+direction] != direction:
                    is_valid = False
                    break
                else:
                    ball_pos = ball_pos+direction

            if is_valid:
                output_columns.append(ball_pos)
            else:
                output_columns.append(-1)

        return output_columns


if __name__ == "__main__":
    sln = Solution()
    grid = [[1, 1, 1, -1, -1],
            [1, 1, 1, -1, -1],
            [-1, -1, -1, 1, 1],
            [1, 1, 1, 1, -1],
            [-1, -1, -1, -1, -1]]
    assert sln.findBall(grid) == [1, -1, -1, -1, -1]

    grid = [[-1]]

    assert sln.findBall(grid) == [-1]

    grid = [[1, 1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1],
            [1, 1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1]]

    assert sln.findBall(grid) == [0, 1, 2, 3, 4, -1]
