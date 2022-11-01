#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:11:07 2022

@author: josephbriggs
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time complexity = O(n+m) where n and m are the number of nodes in the 
        linked list.
        
        Space complexity = O(1)
        
        
        '''
        
        
        output = ListNode()
        temp = output
        
        # check the inputs and return one of the lists if one of the inputs
        # has nothing in it.
        if not list1:
            return list2
        if not list2:
            return list1
        
        # establish which node should be the head.
        if list1.val < list2.val:
            temp.val = list1.val
            list1 = list1.next
        else:
            temp.val = list2.val
            list2 = list2.next

        # iterate over the linked list adding nodes to the output list.
        while(list1 and list2):
            temp.next = ListNode()
            temp = temp.next
            if list1.val < list2.val:
                temp.val = list1.val
                list1 = list1.next
            else:
                temp.val = list2.val
                list2 = list2.next

        # if there are some nodes in the linked lists which haven't been added,
        # add them now.
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        
        return output