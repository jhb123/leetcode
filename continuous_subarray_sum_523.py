# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        An O(n) time complexity solution with space complexity O(n). Could
        reduce the space complexity to O(min(n,k)), but the problem only has
        small input


        Problem
        -------
        Given an integer array nums and an integer k, return true if nums has a
        continuous subarray of size at least two whose elements sum up to a
        multiple of k, or false otherwise.

        An integer x is a multiple of k if there exists an integer n such that
        x = n * k. 0 is always a multiple of k.

        Examples
        --------
        Input: nums = [23,2,4,6,7], k = 6
        Output: true
        Explanation: [2, 4] is a continuous subarray of size 2 whose elements
        sum up to 6.

        Input: nums = [23,2,6,4,7], k = 6
        Output: true
        Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose
        elements sum up to 42. 42 is a multiple of 6 because 42 = 7 * 6 and 7
        is an integer.

        Input: nums = [23,2,6,4,7], k = 13
        Output: false

        Constraints
        -----------
          *  1 <= nums.length <= 105
          *  0 <= nums[i] <= 109
          *  0 <= sum(nums[i]) <= 231 - 1
          *  1 <= k <= 231 - 1

        Solution explanation
        --------------------
        The brute force solution to this problem is O( (n-1)! ) in time because
        there are (n-1) continuous sub arrays of size 2, (n-2) continuous sub
        arrays of size 3 and so on, so (n-1)*(n-2)*...3*2*1 summing of the
        elements of the sub arrays would need to be performed. Given that the
        number of elements in the array can be up to 105, this can take 104!
        operations.

        One way to reduce the time complexity to O(n^2) is by creating a new
        array which contains the rolling sum of the input array. For each
        element in this array, compute the modulo of the element with k. If
        This is zero, then you have found a sub array which sums to a mulitple
        of k. If you never find this condition, start again with a new rolling
        sum, but increment the index of where you start from by 1 i.e.

        arr = [1,2,3], k = 5
        i = 0
        sum_arr = [1,3,6]
        mod_arr = [1,3,1]
        i = 1
        sum_arr = [2,5]
        mod_arr = [2,0]

        when the zero is found, return true. This is O(n^2) because you loop
        through the entire array n times for the i = 0, n-1 for i = 1, n-2 for
        i = 2, and so on, so you get the series n + (n-1) + (n-2) + ... 2 + 1
        which is equal to (n^2 + n)/2. The most important factor of this
        formula is the n^2, so you drop the n and the constants.

        This solution is much better than the brute force method, but it can be
        improved to linear time by using a hash table (look up time is O(1)).
        Each time we calculate modulo k, we are calculate the difference
        between the summed number and a multiple of k. We can check if we have
        already added something which introduces this difference by looking for
        k in a hash table. The important detail here is understanding how to
        calculate the sum of an arbitary sub array between index i and index j.

        e.g.
        arr = [1, 1, 0, 2, 3, 5, 1, 0]
        sum_arr = [1, 2, 2, 4, 7, 12, 13, 13]
        mod_arr = [1, 2, 2, 4, 2, 2, 3, 3]
        if i = 0, then the sum is index sum_arr[j]
        if i is 1, then the sum is sum_arr[j]-sum_arr[0]
        if i is 2, then the sum is sum_arr[j]-sum_arr[1]

        each time we calculate an element in the mod array, we can check a hash
        table to see if we already have a sub array equal whose sum modulo k is
        the remainder, and if we have, we can deduce there must be a sub array
        which sums to a multiple of k. if not, add the (i-1)th element of sum
        to the modulo array. This requires us to prepend the arrays with zero.
        e.g.
        arr = [1, 1, 0, 2, 3, 5, 1, 0]
        ...rolling sum function, prepend zero...
        sum_arr = [0, 1, 2, 2, 4, 7, 12, 13, 13]
        modulo_array = [0]

        hash_table = {}

        for i between 1 to n

        i = 1
        sum_arr[i] = 1
        1%5 = 1
        is this in the hash table? no.
        append 1 to modulo array
        append modulo_array[0] to hash_table -> this is [0].

        i = 2
        sum_arr[i] = 2
        2%5 = 2
        is this in the hash table? no.
        append 2 to modulo array
        append modulo_array[1] to hash_table -> this is [0, 1].

        i = 3
        sum_arr[i] = 2
        2%5 = 2
        is this in the hash table? no.
        append 2 to modulo array
        append modulo_array[2] to hash_table -> this is [0, 1, 2].

        i = 4
        sum_arr[i] = 4
        4%5 = 4
        is this in the hash table? no.
        append 4 to modulo array
        append modulo_array[2] to hash_table -> this is [0, 1, 2, 4].

        i = 5
        sum_arr[i] = 2
        7%5 = 2
        the hash table has keys [1, 2, 4]
        is this in the hash table? yes
        A subarray can be made, so return true.


        '''

        summed_array = [0]
        for i in nums:
            summed_array.append(summed_array[-1] + i)

        modulo_array = [0]
        hash_table = {}

        for i in range(1, len(summed_array)):

            num_to_append = summed_array[i] % k

            if num_to_append == 0 and i > 2:
                return True
            if num_to_append in hash_table:
                return True

            modulo_array.append(num_to_append)

            hash_table[modulo_array[i-1]] = 1

        return False


if __name__ == "__main__":

    sln = Solution()
    assert sln.checkSubarraySum([23, 2, 4, 6, 7], 6) is True
    assert sln.checkSubarraySum([0], 1) is False
    assert sln.checkSubarraySum([1, 2, 3], 5) is True
