#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:12:56 2022

@author: josephbriggs
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        output = ListNode(val = 0)
        output_head = output
        c = 0
               
        while l1 or l2 or c:
            
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            summed = a+b+c
            x = summed%10
            c = summed//10 # 
            output_head.val = x
            output_head = output_head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            